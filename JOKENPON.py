#Importações de bibliotecas do python
from time import sleep
from random import randint


#Àrea do menu inicial
print('-=' * 11)

print('JokenPoo')

print('-=' * 11)

#Declarações de variávies
lista =  ('Pedra' 'Papel' 'Tesoura')
computador = randint (0 , 2)

#Menu de opções
print('''Suas Opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual sua jogada ? '))

#Textinho animado
sleep(1)
print('Jooo')
sleep(1)
print('Kennnn')
sleep(1)
print('Pooooooo')
sleep(1)

#Os resultados são informados
print('-=' * 11)
print('O computador escolheu {}'.format(lista[computador]))
#Essa funçao faz com que no format sejam puxados itens dentro de uma lista , nesse caso pedra 0 , papel 1 ,tesoura 2
print('O jogadorescolheu {}'.format(lista[jogador]))
#Essa funçao faz com que no format sejam puxados itens dentro de uma lista , nesse caso o número que o jogador digitou é puxado da lista
print('-=' * 11)



#Estruturas
if computador == 0: #pedra

    if jogador == 0:
        print('Vocês Empataram')

    elif jogador == 1:
        print('O Computador VENCEU !!')

    elif jogador == 2:
        print('O Computador VENCEU !!')

    else:
        print('Opção inválida !!')


elif computador == 1: #papel

    if jogador == 0:
        print('O Jogador VENCEU !!')

    elif jogador == 1:
        print('Vocês EMPATARAM !!')

    elif jogador == 2:
        print('O Jogador VENCEU !!')

    else:
        print('Opção INVÁLIDA')

elif computador == 2: #tesoura

    if jogador == 0:
        print('O jogador VENCEU !!')

    elif jogador == 1:
        print('O Computador VENCEU!!')

    elif jogador == 2:
        print('Vocês EMPATARAM !!')

    else:
        print('Opção INVÁLIDA !!')