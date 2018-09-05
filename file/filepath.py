# encoding:utf-8
__author__ = 'admin'

import oss2
import os

def all_path(dirname):
    result = []

    for maindir,subdir,file_name_list in os.walk(dirname):
        print maindir
        print subdir
        print file_name_list

        for filename in file_name_list:
            apath = os.path.join(maindir,filename)
            result.append(apath)

    return result

print all_path("E:\Python\py-program")
