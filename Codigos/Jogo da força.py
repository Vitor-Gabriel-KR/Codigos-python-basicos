def jogar():
    print('**************************************')
    print('****Bem vindo ao jogo da força********')
    print('**************************************')
    palavra_secreta="banana".upper()
    letras_acertadas=['_','_','_','_','_','_']
    correta=['B','A','N','A','N','A']
    enforcou=False
    acertou=False
    rodadas=0
    erros=0
    erro=[]
    loop=''
    print('jogando ...')
    print('           ')
    while(not enforcou and not acertou):
        print('           ')
        chute=input(str('Qual a letra ? '))
        print('           ')
        chute=chute.strip().upper()
        if(chute in palavra_secreta):
            index=0
            for letra in palavra_secreta:
                if chute==letra:
                    letras_acertadas[index]=letra
                index+=1
        else:
            erros+=1
            print(('Você errou {} vezes'.format(erros)))
            print('caso erre 6 vezes o jogo acaba')
            erro.append(chute)
        enforcou=erros==6
        print(letras_acertadas)
        rodadas+=1
        if erros==6:
            print('Fim do jogo')
            print('você perdeu por ter errado 6 vezes')
            print('Seus erros foram : {}'.format(erro))
            loop=str(input('Quer tentar novamente? (S/N) '))
            if loop== 'S' or loop=='s':
                    jogar()
            else:
                print('Ok, obrigado por jogar!!!')
        if letras_acertadas == correta:
            print('Parabens,Você ganhou o jogo !!!!')
            print('Você errou {} vezes e demorou {} rodadas para ganhar'.format(erros,rodadas))
            break
if(__name__=="__main__"):
    jogar()
     