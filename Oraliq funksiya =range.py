"""
Created on Sun Apr 18 16:28:03 2021

http://telegram.me/developing_programmer


"""
def oraliq(min,max,qadam=1):
    sonlar=[]
    q=1
    while min<max:
        if q%qadam==0:
            sonlar.append(min)
        min+=1
        q+=1
    return sonlar
sonlar=oraliq(0,15,2)
print(sonlar)
min=int(input('min '))
max=int(input('max '))
qadam=int(input('qadam '))