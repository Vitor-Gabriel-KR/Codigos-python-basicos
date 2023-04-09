matriz=[]
val=[]
num1=[]
num2=[]
for m in range(0,9):
    val.append(input('Digite um valor para [{},{}]: '.format(len(num1),len(num2))))
    matriz.append(val[:])
    val.clear()
    if m==2 or m==5 or m==9:
        num1.append(1)
        num2.clear()
    else:
        num2.append(1)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-')

for c in range(0,3):
    print(matriz[c],matriz[c+1],matriz[c+2], end='')
    c+=3
        