#-*-coding:utf-8-*-
# Author:Lu Wei

import sys
import time
a=[11,22,33]
b=a
#值应用次数
print(sys.getrefcount(a))
#python默认递归次数
print(sys.getrecursionlimit())
#输入输出
# sys.stdout.write('123')
# sys.stdout.write('bac')
# \n换行
# \t制表符
# \r回到当前行的起始位置
#print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格
# print('123123213\r',end='')
# print('hahah',end='')
for i in range(101):
    time.sleep(0.5)
    msg='%s%%\r'%i
    print(msg,end='')
