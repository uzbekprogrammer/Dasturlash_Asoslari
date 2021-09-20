"""
Created on Wed Jul  7 22:49:16 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
q=0
class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
    def get_list(self):
        return [self.ism,self.familiya,self.tyil]
        
talaba1=Talaba('Olim','Olimov',2000)
talaba1_get=talaba1.get_list()

talaba2=Talaba('Ali','Mahmudov',2003)
talaba2_get=talaba2.get_list()

talaba3=Talaba('Doston','Toxirov',2002)
talaba3_get=talaba3.get_list()

a=input('Ma\'lumot kiriting\n>>>')

# Mana shu yerda Olim yoki Olimov yoki 2000 degan soz kiritsa  37-qator qaytiishi kerak

try:
    a=int(a)
except ValueError:
    a=a.title()


royxat=[talaba1_get,talaba2_get,talaba3_get]

for talaba in royxat:
    if a in talaba:
        
        q=1
        break
if q==1:
    print(f'Ism {talaba[0]}\nFamiliya {talaba[1]}\nTug\'ilgan yil {talaba[2]}')
else:
    print('Bunaqa hodimimiz yoq')
