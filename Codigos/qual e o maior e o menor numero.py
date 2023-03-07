
a=float(input('Digite um numero'))
b=float(input('Digite um numero'))
c=float(input('Digite um numero'))
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

print('a numero {} e o maior'.format(maior))
print('a numero {} e o menor'.format(menor))
