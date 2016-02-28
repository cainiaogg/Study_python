# -*- coding: UTF-8 -*-
import os
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re

httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener) #调试

posturl = 'http://210.45.210.6/dzjs/login.asp'

# cj = cookielib.LWPCookieJar()  
# cookie_support = urllib2.HTTPCookieProcessor(cj)  
# opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
# urllib2.install_opener(opener)  
Account = "E21314061"
postdata = {
	'user' : Account,
	'pw' : Account,
}

postdata = urllib.urlencode(postdata)

request = urllib2.Request(posturl,postdata)

response = urllib2.urlopen(request)

content = response.read()
content = content.decode('gbk')
content = content.encode('utf-8')
print content
