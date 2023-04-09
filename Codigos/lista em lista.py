tabela=[]
valores=[]
while True:
    valores.append(str(input('Nome: ')))
    valores.append(int(input('Peso: ')))
    tabela.append(valores[:])
    valores.clear()
    
    passe=str(input('Quer continuar? (S/N)'))
    if passe == 'S' or passe=='s':
        print('Ok!')
    elif passe=='N' or passe=='n':
        break

tam=len(tabela)
print('=-=-=-=-=-=-=-=-=-=====-=-=-=-=-=-=-=-=-=-=')
print('{} pessoas foram cadastradas'.format(tam))
for p in tabela:
    if p[1]>=100:
        print('{} esta a cima do peso com {}.0Kg'.format(p[0],p[1]))
    else:
         print('{} esta a abaixo do peso com {}.0Kg'.format(p[0],p[1]))
    

