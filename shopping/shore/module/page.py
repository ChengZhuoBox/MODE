
#-*- coding:utf-8 _*-  
""" 
@author:chengzhuo 
@file: page.py 
@time: 2017/10/30 
"""
import path_1
import json
list_path=''.join((path_1.dict_path['conf'],'/page_list.txt'))
def page():
    try:
        f = open(list_path, 'r', encoding='utf8')
        list = json.loads(f.read())
        f.close()
    except json.decoder.JSONDecodeError:
        f1 = open(list_path, 'w', encoding='utf8')
        f1.write('[]')
        f1.close()
        print('have not page')
        return None
    for i in list:

        print(i)
    choose=input('input your choose page:')
    while choose not in list:
        choose=input('input mistakenly,please again:')
    return choose


if __name__== '__main__':
    page()
    pass