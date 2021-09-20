"""
Created on Tue Aug  3 22:45:25 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
from tkinter import *
top = Tk()
mb= Menubutton ( top, text="condiments", relief=RAISED, bg="red", fg="yellow", font="italic" )
mb.grid()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"] = mb.menu
mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton ( label="mayo", variable=mayoVar )
mb.menu.add_checkbutton ( label="ketchup", variable=ketchVar )
mb.pack()
top.mainloop()