# encoding:utf-8
__author__ = 'admin'
from asyncore import dispatcher
import asyncore

class ChatServer(dispatcher):
    pass

s = ChatServer()
asyncore.loop()