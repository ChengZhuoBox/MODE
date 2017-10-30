
#-*- coding:utf-8 _*-  
""" 
@author:chengzhuo 
@file: json-text.py 
@time: 2017/10/29 
"""
a=123
import json      #不能写函数和类  要写函数和类用pickle

b=json.dumps(a)


print(type(b))
f=open('J_test.txt','w')
f.write(b)
f.close()