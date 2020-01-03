#-*-coding:utf-8-*-
# Author:Lu Wei
import os

#1.文件路径是否存在 T/F
#os.path.exists()
#2.文件大小
#os.stat().st_size
#3.获取一个绝对路径
path=os.path.abspath('a.txt')
print(path)

path1=os.path.dirname(r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan\day14\a.txt')
print(path1)

# os.path.join()#路径的拼接

'''
path=r'D:\a\2\3'
v='n.txt'
print(os.path.join(path,v))


data=os.listdir(path)
for data in data:
    print(data)

path=r'C:\davidlu\PycharmProjects\luwei-Knightsplan'
result=os.walk(path)
print(type(result))
for a,b,c in result:
    #a(字符串),当前查看的目录 b(列表),此目录下的文件夹 c(列表),此目录下的文件
    print(a,b,c)
'''
