with open('input.txt') as file:
    a,b=file.read().split()
a=int(a)
b=int(b)
c=a*b
c=str(c)
with open('output.txt','w') as file:
    file.write(c)
