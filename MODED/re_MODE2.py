
#-*- coding:utf-8 _*-  
""" 
@author:chengzhuo 
@file: re_MODE2.py 
@time: 2017/10/25 
"""


#re方法

import re
# a=re.split('[k,s]','sdsdgsksfkfjfgkljds')
# print(a)


a=re.sub('a..s','az','sadkshojaghshkjajhs')#替换
print(a)


b=re.compile('\.com')#规则

print(b.findall('hsafjgdksasj.comsdaf.com'))

#'-?\d+\.?\d*'       实数的正则表达式
