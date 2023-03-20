print('=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-')
print('caixa eletronico')
print('=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-')
valor=int(input('Qual será o valor a ser sacado? '))
cinquenta=0
vinte=0
dez=0
um=0
while True:
    if valor > 0:
        if valor >20:
            cinquenta+=1
            valor=valor-50
        elif valor < 50 and valor > 19:
            vinte+=1
            valor=valor-20
        elif valor <20 and valor > 9:
            dez +=1
            valor=valor-10
        else:
            um+=1
            valor=valor-1
    else:
        break
print('=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-')
print('Total de {} cédulas de R$50'.format(cinquenta))
print('Total de {} cédulas de R$20'.format(vinte))
print('Total de {} cédulas de R$10'.format(dez))
print('Total de {} cédulas de R$1'.format(um))
print('=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-')
(print('VOlta sempre ao caixa eletronico! Tenha um bom dia !'))
