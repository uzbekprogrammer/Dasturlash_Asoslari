
"""
Created on Mon Apr 19 10:00:19 2021

Mahmudov Abdurahim

http://telegram.me//developing_programmer
"""
sonlar =list(range(3,1000))
tub_sonlar=[]
print('2; ',end='')
q=2
for tub in sonlar:
    for a in range(2,tub):
        if tub%a!=0:
            q=0
        else:
            q=1
            break
    if q==0:
        tub_sonlar.append(tub)
        print(tub,end='; ')
