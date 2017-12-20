# -*-coding: utf-8 -*-

import os

import sys

class spiderplus(object):
	def __init__(self,plugin,disallow=[]):
		self.dir_exploit = []
		self.disallow = ['__init__']
		self.disallow.extend(disallow)
		self.plugin = os.getcwd()+'/'+plugin
		sys.path.append(plugin)

	def list_plusg(self):
		def filter_func(file):
			if not file.endswith(".py"):
				return False
			for disfile in self.disallow:
				if disfile in file:
					return False
			return True
		dir_exploit = filter(filter_func,os.listdir(self.plugin))
		return list(dir_exploit)

	def work(self,url,html):