
#-*- coding:utf-8 _*-  
""" 
@author:chengzhuo 
@file: path_1.py
@time: 2017/10/30 
"""
from os import path
f=path.abspath(__file__)
dict_path={}
dict_path['shopping']=path.dirname(path.dirname(path.dirname(f)))
dict_path['shore']=''.join((dict_path['shopping'],'/shore'))
dict_path['bin']=''.join((dict_path['shore'],'/bin'))
dict_path['conf']=''.join((dict_path['shore'],'/conf'))
dict_path['module']=''.join((dict_path['shore'],'/module'))
dict_path['logger']=''.join((dict_path['shore'],'/logger'))
f=open("__init__.py",'a',encoding='utf8')
if __name__=='__main__':
    print()