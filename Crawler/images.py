# encoding:utf-8
__author__ = 'admin'
import os
import urllib
import urllib2
import re

#获取url
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()

    return html

#创建图片保存文件夹
def mkdir(path):
    path = path.strip()
    """
    判断路径是否存在，存在True，不存在False
    """
    isExists = os.path.exists(path)
    if not isExists:
        print "新建了名字叫做",path,"的文件夹"
        #创建目录操作函数
        os.mkdir(path)
        return True
    else:
        #如果目录存在则不创建，并提示
        print "名为",path,"的文件夹已存在！"
        return False

def saveImage(imagelist,name):
    number = 1
    for imageurl in imagelist:
        splitPath = imageurl.split(".")
        fTail = splitPath.pop()
        if len(fTail) >3:
            fTail = "jpg"
        fileName = name+ "/" + str(number) + "." + fTail
        #对于每张图片地址，进行保存
        try:
            u = urllib2.urlopen(imageurl)
            data = u.read()
            f = open("path","wb+")
            f.write(data)
            print "正在保存一张图片为",fileName
            f.close()
        except urllib2.URLError as e:
            print e.reason

        number += 1

#获取网页中的所有图片地址
def getAllImage(html):
    #利用正则把源代码中的图片地址过滤出来
    reg = r'src="(.+?\.jpg) pic_ext'
    imgre = re.compile(reg)
    imagelist =imgre.findall(html)
    return imagelist


#创建本地保存文件夹，并下载保存图片
if __name__ == "__main__":
    html = getHtml("https://weibo.com/")
    path = "image"
    mkdir(path)
    imagelist = getAllImage(html)
    saveImage(imagelist,path)