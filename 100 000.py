"""
Created on Tue Oct 19 10:16:24 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
a='SalomDunyoHelloWorld'
royxat=[]
for i in a:
    if i.istitle():
        royxat.append(i)

lis=[]

for i in royxat[1:]:
    b,d=a.split(i)
    lis.append(b)
    d=i+d
    a=a.replace(b,'')

lis.append(d)
print(lis)