"""
Created on Wed Jul  7 21:24:51 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
from datetime import datetime
from tkinter import *

oyna= Tk()
oyna.title('Dasturcha :) ')
oyna.geometry('300x300')

natija=Label(text='Natija',bg='white')
natija.place(x=75,y=135,width=150,height=30)

yil=Entry()
yil.place(x=75,y=50,width=150,height=30)

def farq():
    bugun=datetime.today()
    natija.config(text=bugun.year-int(yil.get()))

tugma=Button(text='Hisoblash',bg='grey',command=farq)
tugma.place(x=90,y=90,width=120,height=40)

oyna.mainloop()