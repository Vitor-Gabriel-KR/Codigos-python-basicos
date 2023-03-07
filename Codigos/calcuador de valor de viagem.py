num=float(input('Qual a distancia?'))
if num < 200:
    val=num*0.5
    print('A viagem vai dar R${}'.format(val))
else:
    val=num*0.45
    print('A viagem vai dar R${}'.format(val))