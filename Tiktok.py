import pyautogui
import time

message=input('Nima deb yozmoqchisiz \n>>>')
while True:
    n=input('Necha marta \n>>>')
    try:
        n=int(n)
        break
    except:
        print('Bu yerga son kiritiladi!!!\nQaytadan kiriting')
s=' '

print('Start')

count = 5
while (count!=0):
    time.sleep(1)
    count -= 1
print('\n COMPLATE')

for i in range(1,int(n)):
    pyautogui.typewrite(message+'\n')
