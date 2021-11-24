from functools import lru_cache
#Bu funcsiya ortiqcha cashlarni tozalab dastur tez ishlashiga yordam beradi
@lru_cache
def fib(n):
    #print(f'Calculating {n}')
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
a=fib(500)
print(a)
