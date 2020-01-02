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

- 变量应用计数器

```
sys.getrefcount(a)#本身也算一次
```

- python递归的次数

```
print(sys.getrecursionlimit())
```

- 输入输出

```
sys.stdout.write('123')
sys.stdout.write('bac')
```

```
# \n换行
# \t制表符  制表符：\t(写法是两个字符的组合，但含义上只是一个字符；t-table)
# \r回到当前行的起始位置
```



```
import os,time
#1.读取文件大小（字节）
file_size=os.stat('a.txt').st_size

with open('a.txt',mode='rb') as f:
    sum=0
    while sum<file_size:
        data=f.read(3)
        sum+=len(data)
        #print(data.encode('utf-8'))
        m=int(sum/file_size*100)
        time.sleep(0.2)
        print('%s%%\r'%m,end='')
```

- sys.argv

```
import sys
import shutil


#让用户执行脚本传入要删除的文件路径，在内部帮助用户将目录删除。
#C:/Users/davidlu/PycharmProjects/luwei-Knightsplan/day14/5.模块传参.py D:/test


#获取用户执行脚本时，传入的参数。
#C:/Users/davidlu/PycharmProjects/luwei-Knightsplan/day14/5.模块传参.py D:/test
#sys.argv=[['C:/Users/davidlu/PycharmProjects/luwei-Knightsplan/day14/5.模块传参.py',D:/test]

path=sys.argv[1]

#删除目录
shutil.rmtree(path)
```

- sys.path ---

###### 2.2 os

和操作系统相关的数据。

- os.path.exists(path) 如果path存在，返回True，如果path不存在，返回False
- os.stat('').st_size 文件大小
- os.path.abspath() #获取一个绝对路径

```
path=os.path.abspath('a.txt')#C:\Users\davidlu\PycharmProjects\luwei-Knightsplan\day14\a.txt
print(path)
```

- os.path.dirname()#获取上级目录

```
path1=os.path.dirname(r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan\day14\a.txt')
print(path1)
```

- os.path.jion()#路径拼接

```
path=r'D:\a\2\3'
v='n.txt'
print(os.path.join(path,v))#D:\a\2\3\n.txt
```

- os.listdir() 查看一个目录下的所有文件【第一层】 

```
path=r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan'
data=os.listdir(path)
print(data)
```

- os.walk()查看一个目录下所有层

```
path=r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan'
result=os.walk(path)
print(type(result))
for a,b,c in result:
    #a(字符串),当前查看的目录 b(列表),此目录下的文件夹 c(列表),此目录下的文件
    print(a,b,c)
```



OSOSOSOS

```
os.getcwd()                 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")         改变当前脚本工作目录；相当于shell下cd
os.curdir                   返回当前目录: ('.')
os.pardir                   获取当前目录的父目录字符串名：('..')
os.makedirs('dir1/dir2')    可生成多层递归目录
os.removedirs('dirname1')   若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')         生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')         删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')       列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()                 删除一个文件
os.rename("oldname","new")  重命名文件/目录
os.stat('path/filename')    获取文件/目录信息
os.sep                      操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep                  当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep                  用于分割文件路径的字符串
os.name                     字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")   运行shell命令，直接显示
os.environ                  获取系统环境变量
os.path.abspath(path)       返回path规范化的绝对路径
os.path.split(path)         将path分割成目录和文件名二元组返回
os.path.dirname(path)       返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)      返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)        如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)         如果path是绝对路径，返回True
os.path.isfile(path)        如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)         如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)      返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)      返回path所指向的文件或者目录的最后修改时间
```

补充：

- ​	转义

```
v1=r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan\day14\a.txt'
v2='C:\\Users\\davidlu\\PycharmProjects\\luwei-Knightsplan\\day14\\a.txt'
```

2.3 shutil

```
import shutil
path=sys.argv[1]

#删除目录
shutil.rmtree(path)
```





总结：

- hashlib
- getpass
- random
- os
- sys
- time
- shutil