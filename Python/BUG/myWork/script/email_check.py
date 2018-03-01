# -*-coding: utf-8 -*-
import re

class spider():
	def run(self,url,html):
		pattern = re.compile(r'([\w-]+@[\w-]+\.[\w-]+)+')
		email_list = re.findall(pattern,html)
		if(email_list):
			print(email_list)
			return True

		return False