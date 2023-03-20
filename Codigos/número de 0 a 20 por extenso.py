extenso=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','deiz','onze','doze','treze','catorze','quinze','dezeseis','dezesete','desoito','dezenove','vinte')
controle=0
while True:
    num=int(input('Digite um número entre 0 e 20:'))
    while controle==0:
        if num <0 or num>20:
            num = int(input('Tente novamente,Digite um número entre 0 e 20:'))
        else:
            controle=1
    print('Você digitou o número {}'.format(extenso[num]))
    break  
        
    