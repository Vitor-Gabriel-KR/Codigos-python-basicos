valores=[]
valor=0
num=int(input('Quantos valores que botar?'))
for c in range(0,num):
    valor=int(input('Digite um valor: '))
    valores.append(valor)
print(valores)
print(len(valores))
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print('O 5 esta na lista')
    