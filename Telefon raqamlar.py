"""
Created on Wed Jul 21 22:45:02 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
from random import *
from time import sleep


print('+',end='')

for i in range(1,15):
    sleep(0.5)
    if i==4 or i==6 or i==10:
        print('-',end='')
    elif i==1 or i==2:
        print('9',end='')
    elif i==5:
        print(choice([90,91,93,94,95,97,98,99,33,88]) ,end='')
    elif i==3:
        print('8',end='')
    else:
        print(randint(1,9),end='')