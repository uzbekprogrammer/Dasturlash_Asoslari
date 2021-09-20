"""
Created on Thu May 13 19:05:50 2021

Muallif: Mahmudov Abdurahim

BaD_BoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
a=int(input('1 - sonni kiriting \n>>>'))
b=int(input('2 - sonni kiriting \n>>>'))
while a!=0 and b!=0:
    if a>b:
        a%=b
    else:
        b%=a
    s=a+b
print(s)