
#-*- coding:utf-8 _*-  
""" 
@author:chengzhuo 
@file: calculator.py 
@time: 2017/10/27 
"""
import re

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y




def macth_brackets(r):
    return re.findall('\([^\(,\)]*\)',r)



def macth_mul_and_div(r):
    i=re.search('-?\d+\.?\d*[\*,\/]-?\d+\.?\d*',r)
    if i!=None :
        l=re.findall('-?\d+\.?\d*',i.group())
        sign=re.search('\*|\/',i.group())
        result=count(l,sign)
        r=r.replace(i.group(),str(result))
        d=re.search('\(-?\d+\.?\d*\)|^-?\d+\.?\d*$',r)
        if d==None:

            return macth_mul_and_div(r)
        else:
            return r 
    else:
        return r




def count(x,sign):
    if sign==None or sign.group() =='+':
        return add(eval(x[0]),eval(x[1]))
    elif sign.group()=='*':
        return mul(eval(x[0]),eval(x[1]))
    elif sign.group()=='/':
        return div(eval(x[0]),eval(x[1]))




def macth_add_and_sub(r):
    i=re.search('(-?\d+\.?\d*)(\+?)(-?\d+\.?\d*)',r)
    i=i.group()
    l=re.findall('-?\d+\.?\d*',i)
    sign=re.search('\+',i)
    if len(l)==2:

        result=count(l,sign)
        r=r.replace(i,str(result))
        d=re.search('\(-?\d+\.?\d*\)|^-?\d+\.?\d*$',r)
        if d==None:
            return macth_add_and_sub(r)
        else:

            return r
    else:
        return r





def run(r):
    l=macth_brackets(r)
    while l:
        for i in l:
            result=macth_mul_and_div(i)
            result=macth_add_and_sub(result)
            result=re.search('-?\d+\.?\d*',result).group()
            r=r.replace(i,result)
            l=macth_brackets(r)
    result_md=macth_mul_and_div(r)
    result=macth_add_and_sub(result_md)
    return result
print(  run('90*12+374/4+4*-94.5+7'))
print(macth_add_and_sub('4+9-9-98+9'))