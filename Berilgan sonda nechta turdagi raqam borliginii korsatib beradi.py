"""
Mahmudov Abdurahim

http:\\telegram.me\developing_programmer

"""

son=int(input('Son kiriting \n>>>'))
b=len(str(son))
a=[] 
d=0
for i in range(0,b):
    s=son%10
    son//=10
    a.insert(0,s)
for raqam in set(a):
    print(raqam)
    d=d+1
print(a,f'{d} ta raqam qatnashgan')