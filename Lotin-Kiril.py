"""
Created on Wed Aug  4 21:41:00 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
from transliterate import to_cyrillic,to_latin
from tkinter import *

oyna=Tk()
oyna.title('Lotin-Kiril')

def tarjima(a):
    a=str(a)
    if a.isascii()==True:
        javob=to_cyrillic(a)
    else:
        javob=to_latin(a)
    label=Label(oyna,text=javob)
    label.pack()
label=Label(oyna,text='Matn kiriting/Матн киритинг ')
label.pack()

e=Entry(oyna,width=50,justify = CENTER)
e.pack()



b=Button(oyna,text='♻O\'zgartirish♻',bd=5,bg='gold',activebackground='blue',command=lambda:tarjima(e.get()))
b.pack()

oyna.mainloop()