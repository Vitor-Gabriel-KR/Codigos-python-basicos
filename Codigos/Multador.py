carro=float(input('velocidade do carro'))
if carro>80:
    multa=(carro-80)*7
    print('Você foi multado no valor de R${}, Dirija com cuidado'.format(multa))
else: 
    print('Dirija com segurança')


