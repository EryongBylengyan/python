# encoding:utf-8
__author__ = 'admin'

import os,oss2,sys

#本机路径
basedir = "E:\\Python\\py-program\\Oss\\file"
#目标目录
ossDir = "ossdir"
#阿里云账号
ossAuth = oss2.Auth("LTAIuJAfudGzFrU4", "6L2v49OcxloZ4mjGrx9T14Kk98VHBI")
#bucketName
ossBucket = oss2.Bucket(ossAuth,"oss-cn-beijing.aliyuncs.com","test-lengxuesong")

ee= [1]
ee[0] = 1

#最后一次上传到哪个文件
ff = 'E:\Python\py-program\Oss\estfile\img1.png'

def uploadFile(file):
    remoteName = ossDir+file.replace(basedir,"").replace("\\","/")
    print ("uploading..",file,"remoteName",remoteName)

    if (ee[0]==0 and remoteName == ff):
        ee[0]=1
    if 1 ==ee[0]:
        result = ossBucket.put_object_from_file(remoteName,file)
        print ("http status:{0}".format(result.status))

def list(dir):
    fs = os.listdir(dir)
    for f in fs:
        file=dir+"//"+f;

        if os.path.isdir(file):
            list(file)

        else:
            uploadFile(file)

#调用开始
list(basedir)

