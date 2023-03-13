
p=str(1)
l=str(2)
m=str(3)
n=str(4)
b=str(5)
n=int(input('Digite um numero:'))
n1=int(input('Digite outro numero:'))

t = input ('[1]Somar;[2]multiplicar;[3]maior;[4]novos números;[5]sair do programa:')
t=str(t)
if t==p:
    print(n+n1)
    c=0
elif t==l:
    print(n*n1)
    c=0
elif t==m:
    if n>n1:
        print(n)
        c=0
    else:
        print(n1)
        c=0
elif t==n:
    n=print(int(input('Digite um numero:')))
    n1=print(int(input('Digite outro numero:')))
    c=0
elif t==b:
    print('FIM')
    c=1