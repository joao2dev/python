import random
jogador = int(input('sua escolha: '))
computador = ("pedra, papel, tisoura")
resposta = random.randint(0 , 2)
print(resposta)
if resposta == 0 and jogador == 1:
    print('voce ganhou')
    else:
        print('perdeu')
if resposta == 1 and jogador == 2:
    print('voce ganhou')
    else:
        print('perdeu')
if resposta == 2 and jogador == 0:
    print('voce ganhou')

