"""
Created on Wed Jul  7 22:49:16 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""

class CreditCard:
    def __init__(self,karta_nomi,davlati,pul):
        self.karta_nomi=karta_nomi
        self.davlati=davlati
        self.pul=pul
    def get_info(self):
        return f'Karta {self.karta_nomi}\nBu {self.davlati} kartasi\nKartangizda {self.pul} $ pul bor'
uzcard=CreditCard('Uzcard', 'O\'zbekiston', 25000)
password=7410
urinish=1
while urinish!=4:
    a=int(input('Karta parolini kiriting :\n>>>'))
    if a==password:
        print(uzcard.get_info())
        break
    else:
        print('Parol xato!!!\nQaytadan kiriting')
        
    if urinish==3:
        print('Uch marta xato kiritdingiz kartangiz bloklandi !!!')
        break
    urinish += 1
    