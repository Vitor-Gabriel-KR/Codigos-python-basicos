

nota1=float(input('Digite a primeria nota:'))
nota2=float(input('Digite a segunda nota'))
media=nota1+nota2/2
if media <= 5 :                                                  
    print('REPROVRADO')
elif media >5 and media < 7 :
    print('RECUPERAÇÂO')
else:
    print('APROVADO')