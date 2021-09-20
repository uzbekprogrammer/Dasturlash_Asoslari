"""
Created on Sun Apr 18 12:49:10 2021

@author: User
"""
listlar=[]
setlar={}
n=1
while True:
    a=input(f'{n}-yoqtirgan mashinangizni kiriting \n>>>')
    n+=1
    b=input('Yana kiritishni istaysizmi ha/yo\'q ')
    if b=='yo\'q':
        break
    listlar.append(a.title())
setlar=set(listlar)
for set in setlar:
    print(set,end=' ')