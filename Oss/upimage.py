# encoding:utf-8
__author__ = 'admin'

import oss2,os,sys

def oss(img_key,img_path):
    auth = oss2.Auth("LTAIuJAfudGzFrU4","6L2v49OcxloZ4mjGrx9T14Kk98VHBI")
    endpoint = ""
    bucket = oss2.Bucket(auth,endpoint,"img1.jpg")
    bucket.put_object_from_file(img_key,img_path)



if __name__ == "__main__":
    img_key = str(uuid.uuid4())+".jpg"
    img_path = "E:\\Python\\py-program\\Oss\\estfile"
    #auth = oss2.Auth("LTAIuJAfudGzFrU4","6L2v49OcxloZ4mjGrx9T14Kk98VHBI")
    oss(img_key,img_path)
    try:
        print "upload success!"
    except Exception as e:
        print "upload faile"

