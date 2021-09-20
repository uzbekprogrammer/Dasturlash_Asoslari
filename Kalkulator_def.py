"""
Created on Mon Aug  2 20:45:40 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
def calculator(a):
    # a=input()
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
    print(javob)

if __name__=='__main__':
    calculator()

    
    


#     else:
#         print('Misol xato kiritildi qaytadan kiriting!!!')
#         continue
#     break
# print(f"Javob:\n>>>{javob}")