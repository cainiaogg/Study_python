# -*- coding: UTF-8 -*-
import os
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re

class loginAoj:

	def __init__(self,user,password):
		self.hosturl = "http://icpc.ahu.edu.cn"
		self.posturl = "http://icpc.ahu.edu.cn/OJ/default.aspx"
		self.user = user
		self.header = {
			"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
			"Referer":"http://icpc.ahu.edu.cn/OJ/default.aspx"
		}
		self.password = password
		self.postdata = {
			"__EVENTTARGET":"ctl00$BtnLogin",
			"__EVENTARGUMENT":"",
			"__VIEWSTATE":"/wEPDwUJNzEyNjg3NDcxZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAwUMY3RsMDAkUmJ0bkluBQxjdGwwMCRSYnRuRXgFDGN0bDAwJFJidG5FeAUIY3RsMDAkTVYPD2RmZO43FUCDg8xZhavVVjEN445K+ga/bD4sGmqz9dvsos9J",
			"__VIEWSTATEGENERATOR":"D0E646C9",
			"__EVENTVALIDATION":"/wEdAAZGhaTCHKA5B7+DKsnJ0aD986dSn2g3ClSROshxmLEhzZeBOX+W0ZQNdFUFOUAkVIQRwl2RCSjHiqKwwuFtt2nP+K1uwgp1q21IiZKyfdTChOezgwwXXoBRIA1OhwCn2UX72+IQJQe4pf7xw289FiMaUCsiCya6T2TNL0hZkwc9FA==",
			"ctl00$TUsername":user,
			"ctl00$TPassword":password,
			}

	def main(self):
		cj = cookielib.LWPCookieJar()  
		cookie_support = urllib2.HTTPCookieProcessor(cj)  
		opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
		urllib2.install_opener(opener)  
		h = urllib2.urlopen(self.hosturl)
		self.postdata = urllib.urlencode(self.postdata)
		request = urllib2.Request(self.posturl,self.postdata,self.header)
		response = urllib2.urlopen(request)
		# f = open("test.html","w")
		# f.write(response.read())

class getCode:
	def __init__(self,user,password,begin,end):
		self.begin = begin
		self.end = end
		self.user = user
		self.password = password
		self.username = "caide2b"
		self.main()
	def login(self):
		self.loginaoj = loginAoj(self.user,self.password)
		self.loginaoj.main()

	def judgeId(self,html): 
		request = urllib2.Request(html)
		response = urllib2.urlopen(request)
		html = response.read()
		part = self.username
		part = re.compile(part)
		ans = re.findall(part,html)
		flag = "Accepted"
		flag = re.compile(flag)
		All = re.findall(flag,html)
		if not All:
			return 0
		if len(ans) == 4:
			return 1
		else:
			return 0;

	def getStatusId(self,begin1,end1,ID):#得到本人提交id
		id = []
		cnt = begin1
		while cnt >= end1:
			try:
				url = "http://icpc.ahu.edu.cn/OJ/Solution.aspx?id=" + str(cnt)
				flag = self.judgeId(url)
				print str(cnt)
				if flag == 1:
					id.append(cnt)
				else:
					pass
			except:
				pass
			cnt-=1
		ID += id

	def getProblemId(self,html):
		part = r"Problem.aspx\?id=([\d]*)\""
		part = re.compile(part)
		ans = re.findall(part,html)
		return ans[0]

	def getLanguage(self,html):
		part = r"Compiler:</abbr> ([A-Z]+)"
		part = re.compile(part)
		ans = re.findall(part,html)
		if ans[0] == 'GCC': return ".c"
		elif ans[0] == 'G++': return ".cpp"
		elif ans[0] == 'Java': return ".java"
		elif ans[0] == 'Pascal': return ".pas"
		else: return ".txt"

	def getContent(self,html):
		part = r"<pre class=\"brush:.*?\">([\s\S]*)</pre>"
		part = re.compile(part)
		ans = re.findall(part,html)
		return ans[0]

	def getCode(self,id):
		for ID in id:
			url = "http://icpc.ahu.edu.cn/OJ/Solution.aspx?id=" + str(ID)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			response = response.read()
			response = HTMLParser.HTMLParser().unescape (response.decode ('utf-8'))
			content = self.getContent(response)
			language= self.getLanguage(response)
			problemid = self.getProblemId(response)
			path = os.getcwd() + '/AojCode'
			print path
			if not os.path.exists(path):
				os.mkdir(path)
			filename = str(problemid) + str(language)
			filename = path+'/'+filename
			f = open(filename,"w")
			f.write(content.encode('utf-8'))
			f.close()
	def main(self):
		self.login()
		id = []

		threads = []
		L = self.begin - self.end
		L /= 10
		while self.end + L< self.begin:
			t = threading.Thread(target = self.getStatusId,args=(self.end + L,self.end,id))
			threads.append(t)
			self.end = self.end + L + 1
		t = threading.Thread(target = self.getStatusId,args = (self.begin,self.end,id))
		threads.append(t)
		for i in threads:
			i.start()
		for i in threads:
			i.join()

		self.getCode(id)

import threading
def gao(begin,end):
	a = getCode("username","password",begin,end)

if __name__ == '__main__':
	gao(225052,114489)