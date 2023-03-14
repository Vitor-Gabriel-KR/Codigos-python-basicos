m=0
s=0
b=0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n>0:
        while m!=10:
            m+=1
            s=n*m
            print('{} x {}={}'.format(n,m,s))
            s=0
        b=input('Quer continuar? S/N-')
        if b=='N':
            break   
    else:
        print('Não aceitamos valores negativos')
        break
