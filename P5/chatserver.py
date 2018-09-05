# encoding:utf-8
__author__ = 'admin'
import socket
import asyncore
from asyncore import dispatcher
from asynchat import async_chat

PORT = 5005
NAME = "TestChat"

class EndSession(Exception):
    pass

class CommandHandler:
    """
    类似于标准库中cmd.cmd的简单命令处理程序
    """

    def unknow(self,session,cmd):
        session.push("unknow command:%s \r\n" % cmd)

    def handle(self,session,line):
        if not line.strip():
            return
        parts = line.strip("",1)
        cmd = parts[0]
        try:
            line = parts[1].strip()
        except IndexError:
            line = ""

        meth = getattr(self,"do_" + cmd,None)
        try:
            meth(session,line)
        except TypeError:
            self.unknow(session,cmd)

class Room(CommandHandler):
    """
    包括一个或多个用户的泛型环境。他负责基本的命令处理和广播。
    """
    def __init__(self,server):
        self.server = server
        self.sessions = []

    def add(self,session):
        self.sessions.append(session)

    def remove(self,session):
        self.sessions.remove(session)

    def broadcase(self,line):
        for session in self.sessions:
            session.push(line)

    def do_logout(self,session,line):
        raise EndSession

class LoginRoom(Room):
    """
    为刚连接的用户准备房间
    """
    def add(self,session):
        Room.add(self,session)
        self.broadcase("Welcome to %s/r/n" % self.server.name)

    def unknow(self,session,cmd):
        self.push('Please log in \n Use "Login<nick>"\r\n')

    def do_login(self,session,line):
        name = line.strip()
        if not name:
            session.push("Please input a name\n")

        elif name in self.server.users:
            session.push('The name %s is taken.\r\n' % name)

        else:
            session.name = name
            session.enter(self.server.main_room)

class ChatRoom(Room):
    """
    为多用户相互连通准备房间
    """
    def add(self,session):
        self.broadcase(session.name+"has entered the room.\r\n")
        self.server.users[session.name] =session
        Room.add(self,session)

    def remove(self,session):
        Room.remove(self,session)
        self.broadcase(session.name+"has letf the room.\r\n")

    def do_say(self,session,line):
        self.broadcase(self.name+":"+line+"\r\n")

    def do_look(self,session,line):
        session.push('THe following are in this room:\r\n')
        for other in self.sessions:
            session.push(other.name+"\r\n")

    def do_who(self,session,line):
        session.push('The following are logged in :\r\n')
        for name in self.server.users:
            session.push(name+'\r\n')

class LogoutRoom(Room):
    """
    为单用户准备的简单房间，致用户将用户名从服务器移除。
    """
    def add(self,session):
        try:
            del self.server.users[session.name]
        except KeyError:
            pass

class  ChatSession(async_chat):
    """
    单会话，负责和单用户通信。
    """
    def __init__(self,server,sock):
        async_chat.__init__(self,sock)
        self.server = server
        self.set_terminator("\r\n")
        self.data = []
        self.name = None
        self.enter(LoginRoom(server))

    def enter(self,room):
        try:
            cur = self.room
        except AttributeError:
            pass
        else:
            cur.remove(self)
        self.room = room
        room.add(self)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = "".join(self.data)
        self.data = []
        try:
            self.room.handle(self,line)
        except  EndSession:
            self.handle_close()

    def handle_close(self):
        async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))


class ChatServer(dispatcher):
    """
    只有一个房间的聊天。
    """
    def __init__(self,port,name):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind("192.168.1.238",port)
        self.listen(5)
        self.name = name
        self.users = {}
        self.main_roor = ChatRoom(self)

    def handle_accept(self):
        conn,addr = self.accept()
        ChatSession(self,conn)

if __name__ == "__main__":
    s = ChatServer(PORT,NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print "Error!"

