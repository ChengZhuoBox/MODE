
#-*- coding:utf-8 _*-  
""" 
@author:chengzhuo 
@file: user.py
@time: 2017/10/30 
"""
import path_1
import json
user_file_path=path_1.dict_path['conf']+'/user.txt'
def log_up():
    f=open(user_file_path,'r',encoding='utf8')
    data=json.loads(f.read())
    user_name=input('input username please:')
    while user_name in data.keys():
        user_name=input('username have existed already,please again')

    user_password=input('input password please:')
    user_password_confirm=input('confirm password:')

    while user_password!=user_password_confirm:
        print('The two inputs is inconsistent,please again')
        user_password = input('input password please:')
        user_password_confirm = input('confirm password:')

    data[user_name]=user_password
    f.close()
    f=open(user_file_path,'w',encoding='utf8')
    f.write(json.dumps(data))
    f.close()

def log_in():
    f=open(user_file_path,'r',encoding='utf8')
    data=json.loads(f.read())
    user_name=input('input username please.if you have not account,please input \'log_up\':')

    if user_name=="log_up":
        f.close()
        log_up()
        print('log in again')
        log_in()
    user_password = input('input password please:')

    while user_name not in data.keys() or data[user_name]!=user_password :
        print('username or password input mistakenly,please again')
        user_name=input('input username please:')
        user_password = input('input password please:')
    f.close()
    print('log in sucess' )



if __name__=='__main__':
    print()
    log_in()
