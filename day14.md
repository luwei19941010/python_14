### day14

#### 今日内容：

- 带参数的装饰器：flask框架+django缓存+写装装饰器实现被装饰的函数要执行N次。
- 模块
  - os
  - sys
  - time
  - datetime
  - timezone

#### 内容回顾&补充

##### 1.函数

写编程的方式：面向过程--->函数式编程-->面向对象编程

###### 1.1特殊参数：补充

补充：对于函数的默认值慎用可变类型。

```
#如果想要给value设置默认参数为空列表
#不推荐
def func（data,value=[]):
	pass
	
#推荐
def func(data,value=None):
	if not value:
		value=[]

```

```
def func(data,value=[]):
	value.append(data)
	return value
v1=func(1)#[1,]
v2=func(1,value=[11,22,33])# 个人理解 [11,22,33,1] 
v3=func(2)#[1,2,] 由于没有传入自己的列表，使用函数默认定义的列表，由于之前被v1同样使用过使用列表内存入了[1,2]


def func(data,value=[]):
	a=value.append(data)
	print(a)
v1=func(1)#none,[1,]
v2=func(1,value=[11,22,33])#none,个人理解 [11,22,33,1]
v3=func(2)#none,[1,2,] 

见下图：
```

![image-20200101145405872](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200101145405872.png)



###### 1.2闭包

```
#不是闭包
def func1(name):
	def inner(*args,**kwargs):
		return 123
	return inner
#是闭包，封装值+内层函数需要使用。
def func2(name):
	def inner(*args,**kwargs):
		print(name)
		return 123
	return inner
```

###### 1.3 递归

```
def func(arg)：
	if a==5:
		return 1000
	result=func(arg+1)+10
	return result
v=func(1)
流程见下图
```

![image-20200101161824948](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200101161824948.png)

```
def func(arg)：
	if a==5:
		return 1000
	result=func(arg+1)+10
	
v=func(1)#只有a=4的那个func能收到返回值1000，其他都是None
```

2.模块

- hashlib
- random
- getpass
- time





###### 1.4装饰器

```
def func(arg):
	def inner (*args,**kwargs):
		return func(*args,**kwargs)
	return inner 
	
@func
def index(a1):
	pass
	
index()

'''
a=func(index(a1))
index=a  #inner
index()
'''
```

#### 内容详细 

##### 1.带参数的装饰器

```
###不带参数的装饰器
#第一步：执行ret=xxx(index)
#第二步：将返回值复制给 index=ret
def xxx(arg):
	def inner(*args,**kwargs):
	ret=arg(*args,**kwargs)
	return ret
return inner

@xxx
def index():
pass


###带参数的装饰器
#第一步:先执行v1=uuu(9)
#第二步：ret=v1(index)
#第三步：index=ret

@uuu(9)
def index():
	pass

```

练习题：

@func1，虽然被装饰函数没有调用，但是装饰器func1就会被执行

```
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
    
=============注意：截止代码到此如果运行代码时，func1就会被执行================
结果：
'''
func1
'''
```

@func（8）虽然被装饰函数没有调用，但是装饰器会在代码执行时执行。

```
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
===============注意：截止代码到此如果运行代码时，func(8)就会被执行=================
结果：
'''
func
func1
'''
```



```
####写一个带参数的装饰器，蚕食是多少，被装饰的函数就要执行多少次，把每次执行的结果添加到列表中，最终返回列表

def func(n):
    def func1(m):
        l=[]
        def inner():
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
```

##### 2.模块

###### 2.1sys

​	python 解释器相关的数据。

```
sys.getrefcount(a)
```