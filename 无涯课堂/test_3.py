#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 反射
# 根据字符串的形式去某个模块中寻找东西--->getattr()
# 根据字符串的形式去某个模块中判断东西是否存在--->hasattr()
# 根据字符串的形式去某个模块中设置东西--->setattr()
# 根据字符串的形式去某个模块中删除东西--->delattr()

import time as t
# 获取时间戳
# print(t.time())
# print(int(t.time()))
# 获取当前时间
# print(t.localtime(t.time()))
# print(t.strftime('%y-%m-%d %H:%M:%S',t.localtime()))

import os
# 创建文件夹
# os.mkdir('e:/log')
# 删除文件夹
# os.rmdir('e:/log')
# 对文件或者目录重新命名
# os.rename('e:/log2','e:/log')
# 对目录的处理
# print('当前文件的目录：',os.path.dirname(__file__))
# print('当前文件的上一级目录：',os.path.dirname(os.path.dirname(__file__)))
# print('当前文件的上两级目录：',os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
# 打开其他文件
# base_dir = os.path.dirname(__file__)
# new_dir = os.path.join(base_dir,"test_1.py")
# f = open(new_dir,'r', encoding="utf-8")
# print(f.read())

import sys
# print(sys.version)
# print(sys.platform)
# for item in sys.path:
#     print(item)
# sys.path.append(’引用模块的地址')

# 序列化：把python的数据类型转为str的类型过程
# dict--->str
# dict_str = json.dumps(dict1)
# list--->str
# list_str = json.dumps(list1)

# 反序列化：把str的类型转为python的数据结构
# str--->dict
# str_dict = json.loads(dict_str)
# str--->list
# str_list = json.loads(list_str)
# 注：tuple反序列化后是列表

# 文件的序列化和反序列化
# 对文件序列化--->就是把服务端的响应数据写到文件中
'''
字符串在Python内部的表示是unicode编码
编码是一种用一种特定的方式对抽象字符（Unicode）转换为二进制形式（bytes）进行表示，也就是python3中的encode。
解码就是对用特定方式表示的二进制数据用特定的方式转化为Unicode，也就是decode。
decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。

如果字符串是这样定义：s=u'中文'则该字符串的编码就被指定为unicode了，即python的内部编码，而与代码文件本身的编码无关。因此，对于这种情况做编码转换，
只需要直接使用encode方法将其转换成指定编码即可。如果一个字符串已经是unicode了，再进行解码则将出错，因此通常要对其编码方式是否为unicode进行判断：
Python 3中基本的str就是unicode，所以可以直接判断str：
isinstance('s', str)
用非unicode编码形式的str来encode会报错

带‘b‘前缀的单引号活双引号表示bites类型的数据
在python 3 中字符是以Unicode的形式存储的，当然这里所说的存储是指存储在计算机内存当中，如果是存储在硬盘里，
Python 3的字符是以bytes形式存储，也就是说如果要将字符写入硬盘，就必须对字符进行encode。
如果要将str写入文件，如果以‘w’模式写入，则要求写入的内容必须是str类型；如果以‘wb’形式写入，则要求写入的内容必须是bytes类型。

总结  
字符串数据类型encode成bytes类型
bytes类型要decode成unicode(str)才能json.dump写入硬盘
读取文件要json.load后反序列化成数据类型
'''
import requests
import json
r =requests.get(url = 'http://www.weather.com.cn/data/sk/101190408.html')
a = r.content
print(type(a))
print(type(r.content.decode('utf-8')))
json.dump(r.content.decode('utf-8'),open('weather.json','w'))

# 对文件的反序列化：就是读取文件的内容
print(type(json.load(open('weather.json','r'))))
dict1 = json.loads(json.load(open('weather.json','r')))
print(dict1['weatherinfo']['city'])
print(dict1,type(dict1))

# md5加密
# 对请求参数ascii编码排序
dict1 = {'name':'wuya','age':18,'city':'xian','work':'tester'}
dict1 = dict(sorted(dict1.items(),key = lambda item:item[0]))
print(dict1)
# 做encode编码
from urllib import parse
datas = parse.urlencode(dict1)
print(datas)
import hashlib
md5 = hashlib.md5()
md5.update(datas.encode('utf-8'))
print(md5.hexdigest())

def getMd5(**kwargs):
    dict1 = dict(sorted(kwargs.items(),key = lambda item:item[0]))
    datas = parse.urlencode(dict1)
    md5 = hashlib.md5()
    md5.update(datas.encode('utf-8'))
    return md5.hexdigest()
print(getMd5(name='wuya',age=18))