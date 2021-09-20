"""
Created on Mon Aug  2 20:29:47 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("BaD BoY Clock")


def time():
	string = strftime('%H:%M:%S')
	label.config(text=string)
	label.after(1100,time)

label = Label(root, font=("simsun", 100), background = "white" , foreground= "black")
label.pack(anchor = 'nw')
time()


mainloop()


