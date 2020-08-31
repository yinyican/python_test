# 字符串
# str = 'admin'
# # 判断以什么开头/结尾
# print(str.startswith('a'))
# print(str.endswith('a'))
# # 判断内容是不是数字
# print(str.isdigit())
# # 小写变大写/小写
# print(str.upper())
# print(str.lower())
# # 以某符号拆分成列表
# str1 = '你好，无涯'
# print(str1.split('，'))
# # 列表转成字符串
# print("，".join(str1.split('，')))
# # 字符串格式化    d是int类型   s字符串类型(兼容性强)
# name = 'wuya'
# age = 18
# print('我的名字是%s,我今年%s岁'%(name,age))
# print('我的名字是{0},我今年{1}岁'.format(name,age))
# print('我的名字是{name},我今年{age}岁'.format(name = name,age = age))

# 列表
# list = [1,99,23,44,100,0.100678,100]
# list_2 = [0,0,0]
# list.insert(0,0)
# print(list)
# list2 = list.copy()
# print(list2)
# print(list.count(100))
# print(list.index(100))
# list.remove(100)
# print(list)
# list.pop()
# print(list)
# list.extend(list_2)
# print(list)
# list.reverse()
# print(list)
# list.sort()
# print(list)
# list = [1,99,23,44,100,0.100678,100]
# for i in list:
#     if i >2:
#         print(i)
# print([x+1 for x in list if x > 2])

# 元组 （不可变，里面的对象可变）
# tuple = (1,5,6,['wuya',18],{'name':'name','age':18})
# tuple[3][0] = 'admin'
# print(tuple)

# 字典
# dict = {'name':'wuya','age':18}
# dict2 = dict.copy()
# print(dict2)
# dict2.clear()
# print(dict2)
# print(dict.get('age'))
# for key,value in dict.items():
#     print(key,value)
# dict2 = {'adress':'xian'}
# dict.update(dict2)
# print(dict)
# # 查看字母的asII码
# print(ord('a'))
# # 对字典key,value(keyasII大小)排序
# print(sorted(dict.items(),key=lambda item:item[0]))

# items()函数作用: 以列表返回可遍历的(键, 值)元组数组。
# dict = {"sb":[{'name':'wuya','age':"18"},{'name':'wuya2','age':"182.2"},{'name':'wuya3','age':"183"}]}
# for i in dict["sb"]:
#     for key,value in i.items():
#         if 'name' in i:
#             if key == 'age':
#                 print(key,':',value)
#                 # 字符串转成浮点数方便比较大小
#                 print(float(value))

# # str ————》list
# str = '9.6'
# str_list = str.split('.')
# print(str_list)
# list_str = '.'.join(str_list)
# print(list_str)
# # dict————》list
# dict1 = {'name':'wuya','age':18}
# dict_list = list(dict1.keys())
# # print(dict_list)
# list_dict = dict(enumerate(dict_list))
# print(list_dict)

# 操作文件   文件的路径以及具体的文件，模式，编码

# 动态参数的个数不确定  数据类型不确定    *元组 **字典
# def f1(*args,**kwargs):
#     print(args,kwargs)
