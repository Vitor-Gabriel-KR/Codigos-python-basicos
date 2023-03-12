for c in range (0,8):
    nasc=int(input('Digite sua idade:'))
    ano=nasc-21
    if ano<1:
        print('Não atingiu a maior idade com {} anos'.format(ano))
    else:
        print('Atingiu a maior idade com {} anos'.format(ano))