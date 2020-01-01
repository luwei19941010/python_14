#-*-coding:utf-8-*-
# Author:Lu Wei
# def func(data,value=[]):
# 	value.append(data)
# 	return value
# v1=func(1)#[1,]
# v2=func(1,[11,22,33])
# print(v1)
# print(v2)

'''
def func(n):
    print('func')
    def func1(m):
        print('func1')
        l=[]
        def inner():
            print('inner')
            for i in range(n):
                l.append(m())
            return l
        return inner
    return func1

@func(8)
def index():
    return 88
v=index()
print(v)

'''

def func1(m):
    print('func1')
    n=8
    l=[]
    def inner():
        print('inner')
        for i in range(n):
            l.append(m())
        return l
    return inner


@func1
def index():
    return 88
