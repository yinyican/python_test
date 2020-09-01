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
# str_list = json.dumps(list_str)
# 注：tuple反序列化后是列表

# 文件的序列化和反序列化
# 对文件序列化--->就是把服务端的响应数据写到文件中
import requests
import json
r =requests.get(url = 'http://www.weather.com.cn/data/sk/101190408.html')
json.dump()