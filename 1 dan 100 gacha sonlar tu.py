"""
Created on Sat Jul 17 22:18:35 2021

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
import random
n=100
numbers=list(range(1,n+1))
x = numbers.pop(random.randint(1, n+1))
print(x)

summa = n*(n+1)/2
print(int(summa-sum(numbers)))