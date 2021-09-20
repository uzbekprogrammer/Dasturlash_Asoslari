"""
Created on Sun Jun  6 11:19:42 2021

Muallif: Mahmudov Abdurahim

BaD_BoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
import pickle

talaba1={'ism':'hasan','familiya':'hasanov','tyil':2003,'kurs':2}
talaba2={'ism':'alijon','familiya':'valiyev','tyil':2004,'kurs':1}


with open('info','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)
with open('info','rb') as file:
    talaba1=pickle.load(file)
    talaba2=pickle.load(file)
print(str(talaba1).rstrip(),'\n',str(talaba2).rstrip())