#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:chengzhuo 
@file: re_MODE.py 
@time: 2017/10/24
"""

import re

#元字符'.'通配符，除了换行符
print(re.findall('www.a','wwwhajlkf'))


#元字符'^'只在开始匹配
print(re.findall('^asf','salasf'))


#元字符'$'，只在结尾匹配
print(re.findall('dad$','dadsdgfvh'))


#元字符'*'，重复匹配[0,+oo]
print(re.findall('d*','jfjhddddjhkjoddhj'))

#'+',重复匹配【1，+oo】

#'?',匹配0到1次

#"{}",匹配任意次
print(re.findall('a{1,5}b','sabaabaab'))

#[],字符集,取消元字符的特殊功能除（\,^,-）
print(re.findall('a[1,2,a,f,fs]','asdafsaf'))

#^ in [],取反
print(re.findall('[^1,2,3,4]','142487574526422314'))


#'\'跟元字符去除特殊功能


#\d 匹配数字
#\D 匹配非数字
#\s 匹配任何空白字符
#\S 匹配非空白
#\w 匹配数字和字母
#\W 匹配非数字和字母
#\b 匹配特殊字符的特殊边界

print(re.findall(r'i\b','i ii%ii dasdiiif'))

#()分组
print(re.findall('(abs)','absabsjodhkyabs;ohohiabs'))
#|
print(re.findall('ad1|j','adadaadajjjhfhhjj'))