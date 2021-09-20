"""
Created on Sun Aug 15 22:36:21 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
import time
import pyautogui
block='shutdown -s -t 5'
# password='12232004''

# while True:
#     reply=pyautogui.password('Kompyuter blocklandi ')
#     if reply==password:
#         break
pyautogui.hotkey('win', 'r')
pyautogui.typewrite('cmd')
pyautogui.press('Enter')
pyautogui.typewrite(f'{block}')
pyautogui.press('Enter')
