#-*-coding:utf-8-*-
# Author:Lu Wei
import sys



#让用户执行脚本传入要删除的文件路径，在内部帮助用户将目录删除。
#C:/Users/davidlu/PycharmProjects/luwei-Knightsplan/day14/5.模块传参.py D:/test


#获取用户执行脚本时，传入的参数。
#C:/Users/davidlu/PycharmProjects/luwei-Knightsplan/day14/5.模块传参.py D:/test
#sys.argv=[['C:/Users/davidlu/PycharmProjects/luwei-Knightsplan/day14/5.模块传参.py',D:/test]
import shutil
path=sys.argv[1]

#删除目录
shutil.rmtree(path)