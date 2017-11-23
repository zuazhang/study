# -*- coding: utf-8 -*- 

#此程序为基于TCP连接的对TCP端口进行扫描的程序
import optparse
from socket import *

'''
第二步：
我们生成两个函数：connScan和portScan.
portScan函数以参数的形式接受主机名和目标端口列表
首先尝试用gethostbyname()函数确定主机名对应的IP
地址，然后用connScan函数输出主机名(或IP地址)，并
使用connScan函数尝试逐个连接我们要连接的每个端口
connScan函数接收两个参数:tgtHost和tgtPort，他会去
尝试建立与目标主机和端口的连接，如果成功，将打印
出端口开放的消息，否则打印出关闭
第三步：
为了抓取目标主机上应用的Banner，我们必须先在connScan
函数中插入一些新增的代码。找到开放的端口后我们向他发
送一个数据串并等待回应，跟进收集到的响应，我们就能推
断出目标主机和端口上的应用
'''
def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		#向端口发送数据串并等待回应
		connSkt.send('ViolentPython\r\n')
		results = connSkt.recv(100)

		print '[+]%d/tcp open' % tgtPort
		print '[+]' + str(results)
		connSkt.close()

	except:
		print '[-]%d/tcp closed'% tgtPort

def portScan(tgtHost,tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot Resolve'%s': Unknown host"% tgtHost
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print '\n[+] Scan Results for: '+ tgtNmae[0]
	except:
		print '\n[+] Scan Results for: '+ tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		print 'Scaning port: ' + tgtPort
		connScan(tgtHost,int(tgtPort))
'''
第一步：
这是从用户那里获得主机名和端口，optparse库解析命令行参数
调用optparse.OptionParser()会生成一个参数解析器(option parser)
的实例，接着在parser.add_option中指定这个脚本具体要解析哪个
命令行参数
'''
def main():
	parser = optparse.OptionParser('usage%prog '+\
	  '-H <target host> -p <target port>')
	parser.add_option('-H', dest = 'tgtHost', type = 'string',\
	  help = 'specify target host')
	parser.add_option('-p', dest = 'tgtPort', type = 'string',\
	  help = 'specify taret port[s] separated by comma')

	(options, args) = parser.parse_args()

	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print '[-] You must specify a target host and port[s].'
		exit(0)
	portScan(tgtHost, tgtPorts)
if __name__ == '__main__':
	main()


