# -*- coding: utf-8 -*-
#python�ṩ���������ú����ӱ�׼�������һ���ı���Ĭ�ϵı�׼�����Ǽ���

#raw_input ����
str = raw_input("enter your input :");
print "received input is :",str

#input ����
#input ������ raw_input �����������Ի���������input������������������
#һ����Ч��python���ʽ�������ؽ��

str_1 = input("enter your input : ");
print "received input is :",str_1

#��ζ�дʵ�ʵ������ļ�
#python�ṩ�˱�Ҫ�ĺ����ͷ�������Ĭ������µ��ļ���������

#open����
#������������õĺ���open()��һ���ļ�������һ��file����
#��صĸ��������ſ�һ���������ж�д
#��һ���ļ� 
fo = open("foo.txt","wb")
print "name of the file :",fo.name#�����ļ�������
print "closed or not :",fo.closed#����true������ļ��ѱ��رգ�����flase
print "opening mode :",fo.mode#���ر����ļ��ķ���ģʽ
print "softspace flag :",fo.softspace#

#close������ˢ�»��������κλ�û��д�����Ϣ�����رո��ļ�����֮��㲻����д��
#��һ���ļ���������ñ�����ָ������һ���ļ�ʱ��python��ر�֮ǰ���ļ���
#��close���������ر��ļ���һ���ܺõ�ϰ��

#�ر����Ĵ򿪵��ļ�
fo.close()

'''
Write()�����ɽ��κ��ַ���д��һ���򿪵��ļ�����Ҫ�ص�ע����ǣ�python�ַ���
�����Ƕ��������ݶ�������������
�¶˴����еĻ��з���\n����ʹ�ü��±����ļ�ʱ����û�л��С�������notepad++
��ʱ���л��С�
'''
fo = open("foo.txt","wb")
fo.write("python is a great language.\nYeah its great!!!\n");
fo.close()

'''
read()��������һ���򿪵��ļ��ж�ȡһ���ַ�������Ҫ�ص�ע����ǣ�python
�ַ��������Ƕ��������ݣ���������������
�÷����д��ݵĲ�����Ҫ���Ѵ򿪵��ļ��ж�ȡ���ֽڼ������÷������ļ���
��ͷ��ʼ��ȡ�����û�д�����������ᾡ���ܶ�Ķ�ȡ���ݣ��ܿ�����֪���ļ���ĩβ

'''
fo = open("foo.txt","r+")#Ȩ��Ϊ��д
str_2 = fo.read(10);
print "readed string is : ",str_2
fo.close()
'''
�ļ�λ�ã�
tell���������������ļ��ڵĵ�ǰλ�ã����仰˵����һ�εĶ�д�ᷢ�����ļ���ͷ
��ô���ֽ�֮��  seek(offset[,from])�����ı䵱ǰ�ļ���λ�ã�offset�������ʾ
Ҫ�ƶ����ֽ�����from����ָ����ʼ�ƶ��ֽڵĲο�λ��
���fromΪ0������ζ�Ž��ļ��Ŀ�ͷ��Ϊ�ƶ��ֽڵĲο�λ�ã������Ϊ1����ʹ��
��ǰ��λ����Ϊ�ο��������Ϊ2����ô���ļ���ĩβ����Ϊ�ο�λ��
'''
fo = open("foo.txt","r+")
str_3 = fo.read(11);
print "read string is :",str_3

#���ҵ�ǰλ��
position = fo.tell();
print "current file position :",position
#��ָ���ٴ��ض�λ���ļ���ͷ
position = fo.seek(0,0);
str_4 = fo.read(12);
print "again read string is :",str_4
fo.close()



































