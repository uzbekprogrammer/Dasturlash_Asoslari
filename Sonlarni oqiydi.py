s={0:"",100:"yuz ",1000:"ming ",1000000:"million " , 1000000000:"milliard "}
S1={0:"",1:"o'n ",2:"yigirma ",3:"o'ttiz ",4:"qirq ",5:"ellik ",6:"oltmish ",7:"yetmish ",8:"sakson ",9:"to'qson "}
S={0:"",1:"bir ",2:"ikki ",3:"uch ", 4:"to'rt ", 5:"besh ",6:"olti ", 7:"yetti ",8:"sakkiz ",9:"to'qqiz "}
s1=""
n=int(input())
r=0; b=0; t=0; f=0; k=0;m=0;m1=0;m2=0;m3=0

while n>0:
    t += 1; f += 1;b += 1;   m += 1;
    r = n % 10;
    n = n // 10;
    if t>=10 and r!=0 and m3==0: m3=1;s1=s[1000000000]+s1
    if t >= 7 and t <= 9 and r != 0 and m2 == 0: m2 = 1;s1 = s[1000000] + s1;
    if t >= 4 and t <= 6 and r != 0 and m1 == 0: m1 = 1;s1 = s[1000] + s1;
    if (t == 3 or f == 3) and r != 0: f = 0;  b = 0;s1 = s[100] + s1;
    if f==3: f=0;b=0

    if b==2 and r!=0: b = 0; s1=S1[r]+s1;
    elif r!=0: s1=S[r]+s1

print(s1)