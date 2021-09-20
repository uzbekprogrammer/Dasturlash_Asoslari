"""
Created on Wed Aug 25 22:08:59 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
from tkinter import *
from tkinter import messagebox
import random
from Kalkulator_def import calculator


root=Tk()
root.title('Imtihon')

c=['+','-','*','//','**']

a=random.choice(list(range(1,10)))
b=random.choice(list(range(1,10)))
e=random.choice(c)
misol=f'{a}{e}{b}'

def bos():
    global misol
    global entry
    javob=calculator(misol)
    if int(entry.get())==javob:
        label1.config=Label(text=f'Correct {javob}')
    else:
        label1.config=Label(text=f'Error {javob}')



label=Label(root,text=misol).pack()

entry=Entry(root).pack()

button=Button(root,text="Barobar",bd=4,bg='blue',activebackground='red',command=bos).pack()

label1=Label(root,text='').pack()
root.mainloop()