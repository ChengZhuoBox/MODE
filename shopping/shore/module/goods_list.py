
#-*- coding:utf-8 _*-  
""" 
@author:chengzhuo 
@file: goods_list.py 
@time: 2017/10/30 
"""
import json
import path_1 as pt




list_path=''



def path_list(page):
    global list_path
    list_path=''.join((pt.dict_path['conf'],'/',page,'_list.txt'))





def check():
    T = False
    try:
        f = open(list_path, 'r', encoding='utf8')
        data = json.loads(f.read())
    except json.decoder.JSONDecodeError:
        f1 = open(list_path, 'w', encoding='utf8')
        f1.write('{}')
        T = True
        f1.close()
    if T:
        data = json.loads(f.read())
    j=1
    for i in data.keys() :

        print(' '.join((str(j)+'.',i,data[i])))
        j+=1
    f.close()
    return data



def add_goods():
    print('add goods or change price of goods')
    T = False
    try:
        f = open(list_path, 'r', encoding='utf8')
        data = json.loads(f.read())
    except json.decoder.JSONDecodeError:
        f1 = open(list_path, 'w', encoding='utf8')
        f1.write('{}')
        T = True
        f1.close()
    if T:
        data = json.loads(f.read())
    T=True
    while T:
        goods=input('input name of goods:')
        goods_2=input('confirm name of goods:')
        price=input('input price of goods:')
        price_2=input('confirm price of goods:')
        while goods != goods_2 or price != price_2:
            print('The two inputs is inconsistent,please again')
            goods = input('input name of goods:')
            goods_2 = input('confirm name of goods:')
            price = input('input price of goods:')
            price_2 = input('confirm price of goods:')
        data[goods]=price
        exit=input('continue add goods,please input \'c\',exit input \'e\':')
        if exit=='e':
            T=False
    f.close()
    f=open(list_path,'w',encoding='utf8')
    f.write(json.dumps(data))
    f.close()






if __name__=="__main__":
    path_list('book')
    add_goods()
    pass