#!/usr/bin/env python
# -*- coding: utf-8 -*-
# char()把数字转换为字母
# ord()把字母转换为数字

'''
open()函数的参数：
1、要操作的文件名称
2、以什么样的方式操作文件

r:只读模式
w:只写模式【不可读，不存在就创建，存在就清空内容】
x:只写模式【不可读，不存在就创建，存在就报错】
a:增加模式【可读，不存在就创建，存在只增加内容】
+  可写可读
'''
f = open('test_file','r',encoding="utf-8")
# 读取文件所有内容放在一个列表
# print(f.readlines())
# 只读取一行
# print(f.readline())
# 读取所有
# print(f.read())
# for i in f.readlines():
#     print(i)
# 读取10个字
print(f.read(10))
# 文件上下文处理,自动关闭
with open("test_file","w") as f:
    f.write('wuya')
    f.read()