# -*-coding:utf-8-*-
import zipfile
import threading

#zFile = zipfile.ZipFile("evil.zip")
#zFile.extractall(pwd=secret)
def extractFile(zFile,password):
	'''
	破解方法
	:param zfile:需要破解的文件
	:param password:尝试代码
	:return:
	'''
	try:
		zFile.extractall(pwd=password)
		print("Found Password:",password)
		event.set()
		return password
	except:
		event.wait()
		pass


def main():
	'''
	主函数
	'''
	zFile = zipfile.ZipFile('evil.zip')
	passFile = open('dict.txt')
	for line in passFile.readlines():
		if event.isSet():
			print "END"
			return
		else:
			password = line.strip('\n')
			t = threading.Thread(target=extractFile,args=(zFile,password))
			t.start()


if __name__=='__main__':
	event = threading.Event()
	main()
	



