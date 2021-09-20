"""
Created on Wed Jul 21 22:01:01 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
while True:
    a=input('Misol kiriting:\n>>>')
    
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
        print('Misol xato kiritildi qaytadan kiriting!!!')
        continue
    break
print(f"Javob:\n>>>{javob}")