# encoding:utf-8
__author__ = 'admin'
import requests
import json
import pytest,pytest_html

"""
r = requests.get("http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28")

print r.status_code
print r.headers
print r.headers["content-encoding"]
print r.encoding
print r.json()
print r.json()["data"]["country"]
"""
"""
def test_01():
    r = requests.get("http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28")

    assert r.json()["data"]["country"] == "中国"
    assert "success!"

def test_02():
    """


with requests.session() as s:
    r = s.request("GET","https://www.imysky.com")
    print "请求对象……"
    print "headers:"+ r.request.headers
    print "method:"+ r.request.method
    print "url:"+r.request.url
    print "响应对象……"
    print "status_code:"+ r.status_code
    print "headers："+ r.headers
    #print r.text
    #response = r.json()
    #print response

with requests.session() as ff:
    r1= ff.request("GET","https://github.com",timeout=(3.05,27))
    r2 = ff.request("GET","https://github.com",timeout=5)
    r3 = ff.request("GET","https://github.com",timeout=None)
    print r1.elapsed
    print r2.elapsed
    print r3.elapsed
"""
def test_status_code():
    assert r.status_code == "200"
    assert "success!"
"""
"""
def test_charset():
    assert r.charset == "utf-8"
    assert "success!"
"""