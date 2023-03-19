valores=[]
valor=0
passe=''
while True:
    valor=int(input('Digite um valor:'))
    if valor in valores:
        print('Valor duplicado! Não será adicionado...')
    else:
        valores.append(valor)
    passe=str(input('Quer continuar? S/N '))
    if passe=='S' or passe=='s':
        print('Ok!')
    elif passe=='N' or passe=='n':
        print('=-=-=-=--=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-==')
        print('você digitou os valores {}'.format(valores))
        break
    else:
        ''