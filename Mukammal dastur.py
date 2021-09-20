"""
Created on Tue Jun 15 11:53:44 2021

Muallif: Mahmudov Abdurahim

BaD_BoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
while True:
    n=input('Son kiriting \n>>>')
    try:
        n=int(n)
        x=100/n
    except ValueError:
        print('Butun son kiritmadingiz ')
    except ZeroDivisionError:
        print('Sonni 0 ga bo\'lish mumkin emas!!! ')
    else:
        print(f'x={x}')
        break
