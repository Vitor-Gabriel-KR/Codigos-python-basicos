salario=float(input('Digite seu salario-R$'))
if salario <1.250: 
    novo=salario + salario*10/100 #O 10 e a porcentagem pra alterar
    print('seu salario atual e {} e o novo e {}'.format(salario,novo))
else:
     novo=salario + salario*15/100 
     print('seu salario atual e {} e o novo e {}'.format(salario,novo))