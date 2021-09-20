"""
Created on Wed Apr 14 13:23:56 2021

Mahmudov Abdurahim

http:\\telegram.me\developing_programmer

"""

print('1 dan 100 gacha son oylang ')
a=list(range(1,101))
l=0
h=100
s=0
q=3
print('KIRITILGAN SON\nKattaroq bolsa 0\nTo`g`ri bolsa 1\nKichikroq bo`lsa 2 kiriting')
while q!=1:
    m=(l+h)//2
    q=int(input(f'O\'ylagan soningiz {m} \n>>>'))
    if q==0:
        h=m-1
    elif q==2:
        l=m+1
    s=s+1
print(f'{s} ta urinish bilan topdim')