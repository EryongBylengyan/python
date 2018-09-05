# encoding:utf-8
__author__ = 'admin'

import itchat
import re



itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]
"""for i in friends:
    signature = i["Signature"]
"""
tList = []
for i in friends:
    signature = i["Signature"].replace("","").replace("span","").replace("class","")
    rep = re.compile("1f\d.+")
    signature = rep.sub("",signature)
    tList.append(signature)

text = "".join(tList)

import jieba
wordlist_jieba = jieba.cut(text,cut_all=True)
wl_space_spilt = "".join(wordlist_jieba)


import matplotlib.pyplot as plt
#from wordcloud import  WordCloud
import PIL.Image as Image


print signature

