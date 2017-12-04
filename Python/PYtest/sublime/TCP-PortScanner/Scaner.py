# -*- coding: utf-8 -*- 

#此程序为基于TCP连接的对TCP端口进行扫描的程序
import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)


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
第四步：
	添加线程，为提高效率我们必须引入python多线程，线程是
	一种能提供这类同时执行多项任务的方法。具体到我们这个
	扫描器，我们要修改的是portScan()函数中迭代循环里的代
	码。此处我们将connScan函数作为线程来调用。这样迭代中
	创建的每个线程就能同时执行
	第五步：
	速度有了提升之后，还有一个缺点。connScan函数会在屏幕
	上打印一个输出。如果多个线程同时打印输出，可能会出现
	乱码和失序。为了让一个函数获得完整的屏幕控制权，需要
	使用一个信号量semaphore。一个简单的信号量就能阻止其他
	线程运行。在打印输出前，我们执行一个枷锁操作
	（screenLock.acquire()）。如果信号量还没被锁上，线程
	就有群继续运行，并输出打印到屏幕上。如果信号量已经被
	锁定，我们就只能等待知道有信号量的线程释放信号量
	通过利用信号量，我们现在能够确保在任何给定的时间点上
	只有一个线程可以打印屏幕。在异常处理代码中，位于finally
	关键字前面的是种植阻塞（其他线程）之前需要执行的代码。
'''
def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost,tgtPort))
		#向端口发送数据串并等待回应
		connSkt.send('ViolentPython\r\n')
		results = connSkt.recv(100)
		#加锁操作
		screenLock.acquire()

		print '[+]%d/tcp open' % tgtPort
		print '[+]' + str(results)
		

	except:
		screenLock.acquire()
		print '[-]%d/tcp closed'% tgtPort
	finally:
		screenLock.release()
		connSkt.close()

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
		t = Thread(target=connScan,args=(tgtHost,int(tgtPort)))
		t.start()

		#print 'Scaning port: ' + tgtPort
		#connScan(tgtHost,int(tgtPort))
'''
第一步：
这是从用户那里获得主机名和端口，optparse库解析命令行参数
调用optparse.OptionParser()会生成一个参数解析器(option parser)
的实例，接着在parser.add_option中指定这个脚本具体要解析哪个
命令行参数
'''
def main():
	parser = optparse.OptionParser('usage %prog '+\
	  '-H <target host> -p <target port>')
	parser.add_option('-H', dest = 'tgtHost', type = 'string',\
	  help = 'specify target host')
	parser.add_option('-p', dest = 'tgtPort', type = 'string',\
	  help = 'specify taret port[s] separated by comma')

	(options, args) = parser.parse_args()

	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)

	portScan(tgtHost, tgtPorts)

	
if __name__ == '__main__':
	main()


