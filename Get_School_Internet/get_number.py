# -*- coding: UTF-8 -*-
import os
from login_library import *

First = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','S','T','V','P','Z']
Second = ['0','1','2','3','4','5']
Third = ['12','13','14','15']
Fourth = '14'
Fifth = ['0','1','2']

F = open('number','w')

for first in First:
	for second in Second:
		for third in Third:
			for fifth in Fifth:
				for six in range(0,100):
					Str = first + second + third + Fourth + fifth + str(six/10) + str(six%10)
					F.write(Str+'\n')
					# flag = login_library(Str)
					# if not flag:
					# 	pass
					# else:
					# 	F.write(Str+'\n')
