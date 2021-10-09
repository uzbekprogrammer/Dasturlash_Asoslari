"""
My proect

Son kiritilganda bu sonni tub tub emasligini aniqlab beradi

https://telegram.me/Mahmudov_Abdurahim

"""
a=int(input('Son kiriting -> '))
b=a//2;#Sonni yarmini topib olamiz
i=2;
q=0;
while (i<=b) and (q!=1):
    i=i+1
    if a%i==0 :
        q=1;
if (a==2) or (a==3):
    print("Bu son tub")
elif q==1 :
    print(f"Bu son tub emas {i-1} ga bolinadi")
else :
    print("Bu son tub ")
