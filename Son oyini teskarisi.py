"""
Created on Fri Apr 16 22:46:34 2021

Theme:Son oyini 

Mahmudov Abdurahim

http:\\telegram.me\developing_programmer

GitHub uzbekprogrammer
"""
from random import randint
print('1 dan 100gacha bir son oyladim \nTopishga harakat qilib koring\n>>>',end='')
a=list(range(1,101))
n=randint(1,100)
q=0
s=0
while a!=n or q<7 or s==1:
    q+=1
    
    a=int(input())
    if a<n:
        print('Kattaroq son kiriting\n>>>',end='')
    elif a>n:
        print('Kichikroq son kiriting\n>>>',end='')
    elif a==n:
        s==1
        print('Ofarin')
    elif q>6:
        print(f'Afsus kiritishlar soni ortib ketti\nO`ylangan son {n} edi')
        s=1