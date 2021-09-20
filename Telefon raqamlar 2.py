"""
Created on Wed Jul 21 23:08:03 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
import random 
import time

a=random.randint(1000000, 9999999)
b=random.choice([90,91,93,94,95,97,98,99,33,88])

c=f'+998 {b} {a}'

for i in c:
    time.sleep(1)
    print(f'{i}',end='')
