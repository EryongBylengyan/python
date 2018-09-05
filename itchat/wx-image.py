# encoding:utf-8
__author__ = 'admin'

import itchat
import math
import os
import PIL.Image as Image


itchat.auto_login(hotReload=True)

def get_friends_lists():
    friends = itchat.get_friends(update=True)[0:]
    #print friends
    user = friends[0]["UserName"]
    #print user

    #os.mkdir ("E:\Python\py-program\itchat\user")
    try:
        os.mkdir ("E:\Python\py-program\itchat\user")

    except Exception as e:
        print repr(e)


    return friends,user

def get_friend_image(i,friend,user):
    print (u"get_friend_image:进入函数")
    print (u"get_friend_image：获取img")
    img = itchat.get_head_img(userName=friend["UserName"])
    print (u"get_friend_image：img保存到文件")
    """
    with open(E/Python/py-progra/itchat/user+"/"+str(i)+".jpg","wb") as f:
        f.write(img)
        f.close()
    """
    pwd = os.getcwd()
    try:
        #pwd = os.getcwd()
        print pwd
        with open(user+"/"+str(i)+".jpg","wb")as f:
            f.write(img)
            f.close()
    except Exception as e:
        print pwd
        print "save faile"
        print repr(e)
    print (u"get_friend_image：退出函数")

def count_for_distribution(friends):
    print (u"get_friend_image：退出函数")
    numpic = len(friends)
    numline = math.ceil(math.sqrt(float(numpic)))
    eachsize = int(640/numline)
    print u"共有好友{0}个，每个小图片的边长为{1}，一行共有{2}个图".format(numpic,eachsize,numline)
    print ("count_for_distribution:退出函数")
    return numpic,eachsize,numline

def merge_to_total(friends,user):
    print (u"merge_to_total:开始进入函数")
    print (u"merge_to_total:下面计算布局")
    numpic,eachsize,numline = count_for_distribution(friends)
    print (u"merge_to_total:下面新建一张总图")
    total_image = Image.new("RGBA",(640,640)).convert("RGB")
    print (u"merge_to_total:下面开始遍历子图")
    for (i,friend) in enumerate(friends):
        print (u"遍历中:第{0}个朋友开始了".format(i))
        print(u"下面开始获取第{0}个图片".format(i))
        print (u"fiend type===",type(friend))
        print (u"friend===",friend)
        get_friend_image(i,friend,user)
        print (u"下面开始合并第{0}个图片到总图片".format(i))
        each_to_total(i,friend,numline,eachsize,total_image,user)
        print (u"第{0}个图片处理完成，开始下一个".format(i))

    print (u"merge_to_total:遍历完成，下面开始保存总图")
    total_image.save(user + ".jpg")
    print (u"merge_to_total:退出函数")

def each_to_total(i,friend,numline,eachsize,total_image,user):
    print (u"each_to_total1:进入函数")
    try:
        img = Image.open(user + "/" +str(i) + ".jpg").convert("RGB")

    except IOError:
        print (u"Error: 没有找到文件或读取文件失败")

    else:
        img = img.resize((eachsize,eachsize),Image.ANTIALIAS)

        x = int(i/numline)
        y = i%numline

        print (u"each_to_total2:位置信息{0} {1}".format(x,y))

        total_image.paste(img,(x*eachsize,y*eachsize))

    print (u"each_to_total3:退出函数")


def send_to_user(user,total_image):
    itchat.send_image(user+".jpg","filehelper")


def main():
    friends,user = get_friends_lists()
    print (u"main:已经获取到朋友们的信息了")
    print ('main:共有好友{0}个'.format(len(friends)))
    print (u"main:下面开始生成总图片")
    print ""
    total_image = merge_to_total(friends,user)
    print (u"main:下面把总图片发送给你")
    print ""
    send_to_user(user,total_image)


if __name__=="__main__":
    main()