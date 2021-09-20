"""
Theme : Sonlarni ingliz tilida yozib beruvchi dastur

Mahmudov Abdurahim

http:\telegram.me\developing_programmer.

"""
a=int(input('Son kiriting\n>>>'))
b=len(str(a))
raqamlar=[]
sonlar=[]
for i in range(0,b):
    s=a%10
    a//=10
    raqamlar.append(s)
for i in range(0,b):
    if raqamlar[i]==0:                  
        son=''
    elif raqamlar[i]==1:
        son='one'
    elif raqamlar[i]==2:
        son='two'
    elif raqamlar[i]==3:
        son='three'
    elif raqamlar[i]==4:
        son='four'
    elif raqamlar[i]==5:
        son='five'
    elif raqamlar[i]==6:
        son='six'
    elif raqamlar[i]==7:
        son='seven'
    elif raqamlar[i]==8:
        son='eight'
    elif raqamlar[i]==9:
        son='nine'
    if i==1 or i==4 or i==7 or i==10 or i==13   :
        if raqamlar[i]==0:                  
            son=''
        elif raqamlar[i]==2:
            son='twenty -'
        elif raqamlar[i]==3:
            son='thirty -'
        elif raqamlar[i]==4:
            son='forty -'
        elif raqamlar[i]==5:
            son='fifty -'
        elif raqamlar[i]==6:
            son='sixty -'
        elif raqamlar[i]==7:
            son='seventy -'
        elif raqamlar[i]==8:
            son='eighty -'
        elif raqamlar[i]==9:
            son='ninety -'
        elif raqamlar[i]==1:
            if i==1 or i==4 or i==7 or i==10 or i==13:
                if raqamlar[i-1]==0:
                    son='ten'
                elif raqamlar[i-1]==1:
                    son='eleven'
                elif raqamlar[i-1]==2:
                    son='twelve'
                elif raqamlar[i-1]==3:
                    son='thirteen'
                elif raqamlar[i-1]==4:
                    son='fourteen'
                elif raqamlar[i-1]==5:
                    son='fifteen'
                elif raqamlar[i-1]==6:
                    son='sixteen'
                elif raqamlar[i-1]==7:
                    son='seventeen'
                elif raqamlar[i-1]==8:
                    son='eighteen'
                elif raqamlar[i-1]==9:
                    son='nineteen'
    elif i==2 or i==5 or i==8 or i==11 or i==14:
        if raqamlar[i-1]==0 and raqamlar[i-2]==0:
            son=son+' hundred'
        else : son=son+'hundred and'
    elif i==3:
        if raqamlar[i+1]!=0 and raqamlar[i+2]!=0 and raqamlar[i]!=0:
            son=son+' thousand'
        else : son=son
    elif i==6 :
        if raqamlar[i+1]!=0 and raqamlar[i+2]!=0 and raqamlar[i]!=0:
            son=son+' million'
        else : son=son
    elif i==9:
        if raqamlar[i+1]!=0 and raqamlar[i+2]!=0 and raqamlar[i]!=0:
            son=son+' billion'
        else : son=son
    elif i==12:
        son=son+' trillion'
    if i==2 and sonlar[0]!='' and sonlar[1]!='':
        if son=='':
            son='and'+son  
    sonlar.append(son)
# if sonlar[1]=='one':
#     sonlar[1]=''
#     if sonlar[0]=='one':
#         sonlar[0]='eleven'
#     if sonlar[0]=='':
#         sonlar[0]='ten'
#     elif sonlar[0]=='two':
#         sonlar[0]='twelve'
#     elif sonlar[0]=='three':
#         sonlar[0]='thirteen'
#     elif sonlar[0]=='four':
#         sonlar[0]='fourteen'
#     elif sonlar[0]=='five':
#         sonlar[0]='fifteen'
#     elif sonlar[0]=='six':
#         sonlar[0]='sixteen'
#     elif sonlar[0]=='seven':
#         sonlar[0]='seventeen'
#     elif sonlar[0]=='eight':
#         sonlar[0]='eighteen'
#     elif sonlar[0]=='nine':
#         sonlar[0]='nineteen'
sonlar.reverse()
for son in sonlar:
    if son !='':
        print(son.strip(),end=" ")
