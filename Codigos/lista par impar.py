valores=[]
par=[]
impar=[]
valor=0

num=int(input('Quer adicionar quantos numeros?'))
for c in range (0,num):
    valor=int(input('Digite um valor: '))
    valores.append(valor)
    if valor % 2==0:
        par.append(valor)
    else:
        impar.append(valor)

print('Normal {}'.format(valores))
print('par {}'.format(par))
print('impar {}'.format(impar))
    
