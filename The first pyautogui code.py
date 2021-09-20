"""
Created on Sun Jun 27 08:21:18 2021

Muallif: Mahmudov Abdurahim

BaD_BoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
import pyautogui
currentMouseY = pyautogui.position()
print(f'Sichqoncha turgan joy {currentMouseY}')
screenHeight  =  pyautogui . size ()
print(f'Ekran balandligi {screenHeight}')
# print(type(currentMouseY),'\n',type(screenHeight))
pyautogui.hotkey('пуск','d')
pyautogui.moveTo(21,45)
pyautogui.doubleClick()
input('Istalgan tugmani bosing \n>>>')