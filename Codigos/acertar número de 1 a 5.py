import random
ran=int(random.uniform(0,5))
while 0<1:
    ran=int(random.uniform(0,5))
    num=int(input('Digite um número entre 0 e 5:'))
    if num==ran:
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print('O Número que você digitou ({}) está correto!!!'.format(num))
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        break
    elif num<0 or num>5:
        print('O seu número ({}) não esta entre 0 e 5: tente novamente'.format(num))
    else:
        print('                                         ')
        print(' você errou: o número era {}'.format(ran))
        print('                                         ')
