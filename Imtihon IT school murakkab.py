"""
Created on Thu Jul 15 20:57:19 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
class CreditCard:
    def __init__(self,karta_nomi,davlat,pul,pul_birligi):
        self.karta_nomi=karta_nomi
        self.davlat=davlat
        self.pul=pul
        self.pul_birligi=pul_birligi
        
    def  get_info(self):
        return f'Karta nomi {self.karta_nomi}\nBu {self.davlat} kartasi\nKartada {self.pul} {self.pul_birligi} pul bor'

uzcard=CreditCard('Uzcard', 'O\'zbekiston',2500000,'so\'m')
uzcard_info=uzcard.get_info()
uzcard_pass=7410

VISA=CreditCard('VISA', 'USA', 25000, '$')
VISA_info=VISA.get_info()
VISA_pass=8520

humo=CreditCard('HUMO', 'O\'zbekiston', 120000, 'so\'m')
humo_info=humo.get_info()
humo_pass=9630

qiwi=CreditCard('Qiwi', 'Rossiya', 65000, 'rubl')
qiwi_info=qiwi.get_info()
qiwi_pass=1223

answer=input('Bizda mavjud kartalar "Humo" ,"Uzcard","Qiwi","VISA" \nKarta nomini kiriting \n>>>')

if answer.upper()=='VISA':
    answer=answer.upper()
else:
    answer=answer.lower()

if answer=='uzcard':
    answer=uzcard
    answer_pass=uzcard_pass
elif answer=='VISA':
    answer=VISA
    answer_pass=VISA_pass
elif answer=='humo':
    answer=humo
    answer_pass=humo_pass
elif answer=='qiwi':
    answer=qiwi
    answer_pass=qiwi_pass
else:
    print('Bizda bunday karta kiritilmagan!!!')

urinish=1

while urinish!=4:
    a=int(input('Karta parolini kiriting :\n>>>'))
    if a==answer_pass:
        print(answer.get_info())
        break
    else:
        print('Parol xato!!!\nQaytadan kiriting')
        
    if urinish==3:
        print('Uch marta xato kiritdingiz kartangiz bloklandi !!!')
        break
    urinish += 1
    