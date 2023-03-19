valores=[]
posição=0
val=0
posição2=[0]
org=valores[:]
for v in range(0,5):
    val=int(input('Digite um valor para a posição {}:'.format(posição)))
    posição+=1
    valores.append(val)
    posição2.append(posição)
print('=-=-==-=-=-=-==-=-=-=-=-==-====-=-==-=-===-=-==-=-=-=-=-=-===-=--==-=-=-')
print('Você digitou os valores {}'.format(valores))
org=valores[:]
org.sort()
print('O maior valor digitado foi {} nas posicão {}'.format(org[4],posição2[4]))

print('O menor valor digitado foi {} nas posição {}'.format(org[0],posição2[1]))