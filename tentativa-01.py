from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
2
print('''Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')



player =  int(input('Qual é a sua jogada'))

print('JOOO')
sleep(1)
print('KEEENN')
sleep(1)
print('POOOOOOOOOO')
sleep(1)

print('-=' * 11)

print('O computador escolheu: {}'.format(itens[comp]))
#Essa funçao faz com que no format sejam puxados itens dentro de uma lista , nesse caso pedra 0 , papel 1 ,tesoura 2
print('O jogador escolheu: {} '.format(itens[player]))
#Essa funçao faz com que no format sejam puxados itens dentro de uma lista , nesse caso o numero que o jogador digitou

print('-=' * 11)


if comp == 0 and player == 1 or player == 2: #Pedra
    print('O computador ganhou !!')

elif comp == 1 and player == 0 or player == 2: #Papel
    print('O jogador ganhou')

elif comp == 2 and player == 0 : #Tesoura
    print('O jogador ganhou')

elif comp == 2 and player == 1:
    print('O Computador ganhou !!')

elif comp == 2 and player == 2: #GAMBIARRA
    print('Vocês empataram !! ')

elif comp == player:
    print('Vocês empataram !!')


    #Na Primeira tentativa deu mais ou menos certo kkkk
    #Quando o player escolhe tesoura , não sei o porque, mas o computador sempre ganha .
    #Mesmo que tenha saído 2 vz tesoura
