"""
Created on Thu Jul  1 08:59:46 2021

Muallif: Mahmudov Abdurahim

http://t.me/ 

My portfolio: http://github.com/uzbekprogrammer

"""
from googletrans import Translator
tarjimon=Translator()
matn=input('Tarjima  uchun matn kiriting :\n>>>')
tarjima=tarjimon.translate(matn)
print(tarjima.origin)