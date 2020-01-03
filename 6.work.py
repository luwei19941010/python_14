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


dicta={'a':1,'b':2,'c':3,'d':4,'f':'hello'}
dictb={'b':3,'d':5,'e':7,'m':9,'k':'world'}
dictc={}
for itema in dicta.items():
    a1,a2=itema
    for itemb in dictb.items():
        b1,b2=itemb
        if a1==b1:
            print(a1)
            dictc[a1]=a2+b2
        else:
            dictc[a1]=a2
            dictc[b1]=b2
print(sorted(dictc.items(),key=lambda a:a[0],reverse=False))
'''


#10.看代码写结果
'''
def extendlist(val,list=[]):
    list.append(val)
    return list
list1=extendlist(10)
list2=extendlist(123,[])
list3=extendlist('a')
print(list1,list2,list3)

list1:[10,'a']
list2:[123]
list:[10,'a']
'''
#11.面试题https://gitee.com/old_boy_python_stack_21/teaching_plan/issues/IVGCH
#1.A，B,C
#2.
'''
res={}
a=('a','b','c','d','e')
b=(1,2,3,4,5)
for i in range(len(a)):
    res[a[i]]=b[i]
print(res)
'''
#3.python 代码获取命令行参数
# import sys
# print(sys.argv)
#4.ip='192.168.0.100'
# ip='192.168.0.100'
# data=ip.split('.')
# print(data)
# new_data=[]
# for i in data:
#     new_data.append(bin(int(i)).lstrip('0b').zfill(8))
# print('.'.join(new_data))

#5.
# sum=''
# Alist=['a','b','c']
# for i in range(len(Alist)):
#     sum=sum+Alist[i]
#
# print(','.join(sum))

#6.
# STRA='123143141jahsgdavhgsdvavsj'
# # #最后两个
# # print(STRA[-1:-2:-1])
# #第二个 第三个
# print(STRA[1],STRA[2])

#7.
#print(Alist[0:4]

#8.编写一个函数，让函数接受一个文件夹名称作为参数，显示文件夹中文件的路径，以及其中包含文件夹中文件的路径
# import sys,os
# data=sys.argv
#
# v=os.path.dirname(os.path.abspath(data[0]))
# for a,b,c in os.walk(v):
#     for i in c:
#         print(os.path.join(a,i))
#

#8.
sum = 0
d=[]
for n in range(1,1001):
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        d.append(n)
        sum = 0
    sum=0
print(d)






















