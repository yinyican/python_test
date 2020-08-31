# 匿名函数
# def add(a,b):
#     return a+b
# print(add(2,3))

# 左边形参  右边内容
# per = lambda a,b:a+b
# print(per(2,3))

# 三步运算
# age = 10
# if age >5:
#     print("true")
# else:
#     print("false")
# print('true') if age > 5 else print("false")
#
# # 结合
# login = lambda username,password:print('登陆成功') if username == "wuya" and password == "admin" else print("登录错误")
# login("wuya",'admin')

# 对请求的参数进行ascii排序
# def data(**kwargs):
#     return dict(sorted(kwargs.items(),key=lambda item:item[0]))
# dict1 = {"app_id": "lyCZnSfLCoeeXSNrwk",
#          "version": "1.0",
#         "nonce": 'nonce',
#         "timestamp": 'timestamp'
#        }
# print(data(**dict1))
#
# data2 = lambda **kwargs:dict(sorted(kwargs.items(),key=lambda item:item[0]))
# print(data2(**dict1))

# 将列表中每一个值增加100
list1 = [1,2,3,4,5]
# 第一种

# def f1():
#     list2 = []
#     for i in list1:
#         i+= 100
#         list2.append(i)
#     print(list2)
# f1()

# 第二种
# def f2(a):
#     return a+100
# print(list(map(f2,list1)))
# 第三种
# print(list(map(lambda a:a+100,list1)))

# 条件判断(过滤)
# 第一种
# def f1():
#     list2 = []
#     for i in list1:
#         if i >1:
#             list2.append(i)
#     print(list2)
# f1()
# 第二种
# print(list(filter(lambda a:a>1,list1)))

# 装饰器
# 封闭:对以实现的代码尽可能的不要做修改
# 开放:对现有的功能代码可扩展
# 步骤：
# 1、执行getinfo函数的时候把被装饰的函数f1当非参数来传递
# 2、getinfo函数的返回值会重新赋值
# 3、一旦结合了装饰器后，调用f1的函数其实执行的是inner函数的内部，原来的函数f1被覆盖
# 4、被装饰的函数f1重新赋值给装饰器的内层函数inner
# 简单示例
# def getInfo(func):
#     def inner():
#         print("《Python自动化测试实战》")
#         func()
#     return inner
# @getInfo
# def f1():
#     print('网易云课堂')
# f1()
# 实际应用
def login(func):
    def inner(token):
        if token == 'asdqwe':
            return func(token)
        else:
            return '请登陆系统'
    return inner
@login
def profile(par):
    return "你的主页信息"
print(profile("asdqwe"))
