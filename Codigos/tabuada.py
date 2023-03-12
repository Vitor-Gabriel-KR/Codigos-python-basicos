c=int(input('Digite um numero do qual você quer saber a tabuada:'))
multiplo=int(input('Quer saber até qual multiplo?'))

cont=0
cont2=0
for a in range(0,multiplo):
    cont+=1
    cont2=c * cont
    if cont != multiplo +1:
        print('{} x {} = {}'.format(c,cont,cont2))
    else:
        break