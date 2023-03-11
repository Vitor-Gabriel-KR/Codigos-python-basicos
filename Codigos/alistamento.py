ano=int(input('Digite sua idade:'))
if ano<18:
    calc=ano - 18
    print('Você ainda vai se alistar, faltam {} anos apra isso'.format(calc))
elif ano>18:
   calc2=ano - 18
   print('Já passou o tempo para de alistar, o tempo que passou foi de {} anos'.format(calc2))
else:
    print('você já deve se alistar')