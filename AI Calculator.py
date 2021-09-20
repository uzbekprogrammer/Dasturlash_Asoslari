"""
Created on Wed Aug  4 20:40:20 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
# from Kalkulator_def import calculator
from tkinter import *
oyna=Tk()
oyna.title('AI Calculator')
def calculator(a):
    a=str(a)
    if '+' in a:
        b,d=a.split('+')
        javob=int(b)+int(d)
    elif '-' in a:
        b,d=a.split('-')
        javob=int(b)-int(d)
    elif '//' in a:
        b,d=a.split('//')
        javob=int(b)//int(d)
    elif '**' in a:
        b,d=a.split('**')
        javob=int(b)**int(d)
    elif '*' in a:
        b,d=a.split('*')
        javob=int(b)*int(d)
    elif '/' in a:
        b,d=a.split('/')
        javob=int(b)/int(d)
    
    elif '%' in a:
        b,d=a.split('%')
        javob=int(b)%int(d)
    else:
        javob='Misol xato kiritildi'
    if javob=='Misol xato kiritildi':
        pass
    else:
        javob=f'{a}={javob}'
    label=Label(oyna,text=javob,bg='red',justify=CENTER)
    label.grid(row=2,column=1)

label=Label(oyna,text='Misol kiring')
label.grid(row=0,column=0)

e=Entry(oyna,width=50,justify = CENTER)
e.grid(row=0,column=1)



b=Button(oyna,text='Barobar',bd=5,bg='gold',activebackground='blue',command=lambda:calculator(e.get()))
b.grid(row=1,column=1)


oyna.mainloop()






















