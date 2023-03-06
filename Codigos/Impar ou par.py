num=int(input('Veja se o número e impar ou par:'))
result=num % 2
if result==0:
    print('O número {} e PAR'.format(num))
else:
    print('O número {} e IMPAR'.format(num))