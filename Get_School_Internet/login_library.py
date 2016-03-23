# -*- coding: UTF-8 -*-
import os
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re

def login_library(Account):
	# hosturl = 'http://210.45.210.6/dzjs/login_form.asp'
	posturl = 'http://210.45.210.6/dzjs/login.asp'

	# cj = cookielib.LWPCookieJar()  
	# cookie_support = urllib2.HTTPCookieProcessor(cj)  
	# opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
	# urllib2.install_opener(opener)  

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

	Str = r'欢迎'
	Str = re.compile(Str)

	All = re.findall(Str,content)

	if not All:
		return False
	return True