#-*-coding:utf-8-*-
# Author:Lu Wei


import sys,os

"""
#1.为函数写一个装饰器，在函数执行之后输入 after

def wrapper(arg):
    def inner(*args,**kwargs):
        result=arg()
        print('after')
        return result
    return inner

@wrapper
def func():
    print(123)

func()




#2.为函数写一个装饰器，把函数的返回值 +100 然后再返回。

def wrapper(arg):
    def inner(*args,**kwargs):
        data=arg(*args,**kwargs)+100
        return data
    return inner

@wrapper
def func():
    return 7

result = func()
print(result)



#3.为函数写一个装饰器，根据参数不同做不同操作。

# flag为True，则 让原函数执行后返回值加100，并返回。
# flag为False，则 让原函数执行后返回值减100，并返回。

def x(flag):
    flag=flag
    def wrapper(arg):
        def inner(*args,**kwargs):
            if flag:
                data=arg(*args,**kwargs)+100
            else:
                data=arg(*args,**kwargs)-100
            return data
        return inner
    return wrapper

@x(True)
def f1():
    return 11

@x(False)
def f2():
    return 22

r1 = f1()
r2=f2()
print(r1,r2)
"""

#4.写一个脚本，接收两个参数。
'''
第一个参数：文件
第二个参数：内容
请将第二个参数中的内容写入到 文件（第一个参数）中。


print(sys.argv)
path=sys.argv[1]
data=sys.argv[2]

with open('a.txt',mode='w',encoding='utf-8') as f:
    f.write(data)
    f.flush()
'''

# 执行脚本： python test.py oldboy.txt 你好

#5.递归的最大次数是多少？ #1000

# a=sys.getrecursionlimit()
# print(a)


#6.看代码写结果
# print("你\n好")#你 换行  好
# print("你\\n好")#你\n好
# print(r"你\n好")#你\n好


#7.写函数实现，查看一个路径下所有的文件【所有】。
# path=input('path:')
# data=os.walk(path)
# for a,b,c in data:
#     print('目录:',a)
#     print('列表:',b)
#     print('文件:',c)



#8.写代码
# 请根据path找到code目录下所有的文件【单层】，并打印出来。
# path = r"C:\users\davidlu\PycharmProjects\luwei-Knightsplan"
# data=os.listdir(path)
# print(data)

'''
#9.写代码实现【题目1】和【题目2】
a=1
b=1
l=[1,1]
while b<4000000:
    a=b
    b+=a
    l.append(b)
    print(b)

print(l.index(a))
'''

dicta={'a':1,'b':2,'c':3,'d':4,'e':'hello'}
dictb={'b':3,'d':5}

