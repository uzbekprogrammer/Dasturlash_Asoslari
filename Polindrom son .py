"""
Created on Tue Apr 13 22:07:55 2021

Mahmudov Abdurahim

http:\\telegram.me\developing_programmer

"""
son=int(input('Son kiriting\n>>>'))
a=len(str(son))
raqamlar=[]
sonlar = []
s=''
d=''
for i in range(0,a):
    b=son%10
    son//=10
    raqamlar.append(b)
for raqam in raqamlar:
    s=s+str(raqam)
raqamlar.reverse()
for raqam in raqamlar :
    d+=str(raqam)
if int(s)-int(d)==0:
    print('Bu sonlar polindrom ')
else:
    print('Bu sonlar polidrom emas')
print(s ,end=' ')
print(d)