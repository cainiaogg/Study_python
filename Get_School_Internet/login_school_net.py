# -*- coding: UTF-8 -*-
import os
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re


def login_school_net(Number, Password):

    # cj = cookielib.LWPCookieJar()
    # cookie_support = urllib2.HTTPCookieProcessor(cj)
    # opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    # urllib2.install_opener(opener)  #cookie

    # httpHandler = urllib2.HTTPHandler(debuglevel=1)
    # httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    # opener = urllib2.build_opener(httpHandler, httpsHandler)
    # urllib2.install_opener(opener) #调试

    hosturl = 'http://yunwei.ahu.edu.cn/yunwei/analyze.jsp'
    posturl = 'http://yunwei.ahu.edu.cn/yunwei/oalogin.html'
    # header = {
    # 	'Host':"yunwei.ahu.edu.cn",
    # 	'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
    # 	'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    # 	'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    # 	'Accept-Encoding':"gzip, deflate",
    # 	'Referer':"http://yunwei.ahu.edu.cn/yunwei/oalogin.html",
    # 	'Connection':"keep-alive"
    # }#header

    postdata = {
        "userid": Number,
        "passwd": Password,
        "usertype": "user",
    }

    postdata = urllib.urlencode(postdata)

    request = urllib2.Request(hosturl, postdata)
    response = urllib2.urlopen(request, timeout=1)

    content = response.read().decode('gbk').encode('utf-8')

    S = r'错误'
    S = re.compile(S)
    All = re.findall(S, content)
    if not All:
        return True
    return False

if __name__ == "__main__":
	print login_school_net("I61314002", "123456")
