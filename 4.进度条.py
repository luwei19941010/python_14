#-*-coding:utf-8-*-
# Author:Lu Wei

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
