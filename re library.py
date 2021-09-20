"""
Created on Tue Jul  6 08:53:55 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
import re
from uzwords_sariqdev import words
andoza='^к.т.к$'
matches=[]
for word in words:
    if re.match(andoza,word):
        matches.append(word)
print(matches)