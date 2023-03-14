anos=0
homens=0
mulheres=0
while True:
    b= int(input('Idade:'))
    c=input('Sexo:M/F')
    a=input('Quer continuar? S/N')
    if a=='N':
        break
    elif a=='S':
        ''
if b>18:
    anos+=1
if c=='M':
    homens+=1
if c=='F' and b <20:
    mulheres+=1
print('{} Pessoas tem mais de 18 anos'.format(anos))
print('{} Homens foram cadrastados'.format(homens))
print('{} Mulheres tem menos de 20 anos'.format(mulheres))

    