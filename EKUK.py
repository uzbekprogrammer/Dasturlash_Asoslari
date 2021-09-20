"""
Theme: Number's EKUK

Mahmudov Abdurahim

http:\telegram.me\developing_programmer

mahmudovabdurahim04@gmail.com

"""
# EKUK(a,b)
i=1
q=0
s=0
a=int(input('1 - sonni kiriting '))
b=int(input('2 - sonni kiriting '))
if a<b:
    a,b=b,a
if a%b==0:
    print(f'Bu sonlarning EKUKi {a}')
else:
    while i<=b and q==0:
        s=a*i
        if s%b==0:
            q=1
        i+=1
    print(f'Bu sonlarning EKUKi {s}')
