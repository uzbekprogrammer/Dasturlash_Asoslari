from random import randint
# print('Keling o`ylangan sonni topish o`ynaymiz\n1 dan 10 gacha son o`ylang\n>>>',end='')
rozilik=1
taxmin=15456
a=1
b=10
taxmin_soni=0
fikrim=10
taxmin_soni1=0
while rozilik==1:
    print('Keling o`ylangan sonni topish o`ynaymiz\n1 dan 10 gacha son o`yladim topishga harakat qilib koring\n>>>',end='')
    komp_oylagan=randint(1,10)
    while komp_oylagan!=taxmin:
        taxmin=int(input())
        taxmin_soni+=1
        if taxmin==komp_oylagan:
            print(f'Barakalla siz {taxmin_soni}ta taxmin bilan topdingiz')
            break
        elif taxmin>komp_oylagan:
            print('XATO , men oylagan son bundan kichikroq\n>>>',end='')
            continue
        elif taxmin<komp_oylagan:
            print('XATO , men oylagan son bundan kattaroq\n>>>',end='')
            continue
    print('1 dan 10 gacha son oylang men topishga harakat qilib koraman')
    while fikrim!='t':
        komp_taxmini=randint(a, b)
        taxmin_soni1+=1
        fikrim=input(f'Siz {komp_taxmini} sonini oyladingiz: to`g`ri bo`lsa (t), men oylagan son kattaroq (+),yoki kichikroq (-)')
        if fikrim=='t':
            print(f'O`ylagan soningizni {taxmin_soni1} urinish bilan topdim')
            break
        elif fikrim=='+':
            a=komp_taxmini+1
            continue
        elif fikrim=='-':
            b=komp_taxmini-1
            continue
    if taxmin_soni==taxmin_soni1:
        print(f'Durrang!Ikkimiz ham {taxmin_soni}ta taxmin bilan topdik ')
    elif taxmin_soni1>taxmin_soni:
        print(f'Siz {taxmin_soni}ta urinish bilan topdingiz va yutdingiz')
    elif taxmin_soni>taxmin_soni1:
        print(f'Men {taxmin_soni1}ta urinish bilan topdim va yutdim')
    rozilik=int(input('Yana o`ynaymizmi ha(1)/yo`q(0)'))

    
