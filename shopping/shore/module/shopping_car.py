
#-*- coding:utf-8 _*-  
""" 
@author:chengzhuo 
@file: shopping_car.py 
@time: 2017/10/30 
"""
import json
import path_1
list_path=''.join((path_1.dict_path['conf'],'/shopping_list.txt'))
def check(name):
    T=False
    try:
        f=  open(list_path,'r',encoding='utf8')
        list = json.loads(f.read())
    except json.decoder.JSONDecodeError:
        f1=  open(list_path,'w',encoding='utf8')
        f1.write('{}')
        T=True
        f1.close()
    if T:
        list=json.loads(f.read())
    if name not in list.keys() \
            or list[name]=="" \
            or list[name]['total price']=='0.0'\
            or list[name]['total price']=='0':
        print('your shopping car is empty')
    else:
        list_name=list[name]
        j=1
        for i in list_name.keys():
            if i!= 'total price':
                print(' '.join((str(j) + '.', i, list_name[i])))
                j+=1
        print(' '.join((str(j) + '.', 'total price', list_name['total price'])))
    f.close()




def add_goods(name,goods,price):
    t='total price'
    T=False
    try:
        f=  open(list_path,'r',encoding='utf8')
        list = json.loads(f.read())
    except json.decoder.JSONDecodeError:
        f1=  open(list_path,'w',encoding='utf8')
        f1.write('{}')
        T=True
        f1.close()
    if T:
        list=json.loads(f.read())
    f.close()
    if name not in list.keys():
        list[name]={}
    this_list=list[name]
    this_list[goods]=price
    if t not in this_list.keys():
        this_list[t]=price
    else:
        this_list[t]=str(float(this_list[t])+float(price))
    f=open(list_path,'w',encoding='utf8')
    f.write(json.dumps(list))
    f.close()


def sub_goods(name,goods):
    t = 'total price'
    T = False
    try:
        f = open(list_path, 'r', encoding='utf8')
        list = json.loads(f.read())
    except json.decoder.JSONDecodeError:
        f1 = open(list_path, 'w', encoding='utf8')
        f1.write('{}')
        T = True
        f1.close()
    if T:
        list = json.loads(f.read())
    f.close()
    this_list = list[name]
    price=this_list.pop(goods)
    this_list[t] = str(float(this_list[t]) - float(price))
    f=open(list_path,'w',encoding='utf8')
    f.write(json.dumps(list))
    f.close()

def pay_bill(name):
    







if __name__ == '__main__':
    add_goods('chengzhuo',goods='car',price='1245200114')
    sub_goods('chengzhuo','car')
    check("chengzhuo")
    pass