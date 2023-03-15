sexo=0
c=0
while c!=0:
    sexo=str(input('Digite seu sexo: [M]/[F]'))
    if sexo!='M':
        print('Feminino')
        c+=1
    elif sexo =='M': 
        print('Masculino')
        c+=1
    else:
        print('sexo invalido!!!')
        
