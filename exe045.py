from random import randint

from time import sleep
itens = ('Pedra','Papel','Tesoura')

computador = randint(0,2)
print (''' Suas opcões:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))
if jogador >2:
    print('Jogada INVÁLIDA!\n Jogue novamente')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 12)
print(' Computador jogou {}'.format(itens[computador]))
print(' Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0 :
    if jogador ==0:
        print('Empate')
        print('COMPUTADOR: {} X JOGADOR: {}'.format(itens[computador], itens[jogador]))
    elif jogador ==1:
        print('Você GANHOU!!!')
        print('COMPUTADOR: {} X JOGADOR: {}'.format(itens[computador], itens[jogador]))
    elif jogador == 2:
        print('O computador GANHOU!!!')
        print('COMPUTADOR: {} X JOGADOR: {}'.format(itens[computador], itens[jogador]))
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1 :
    if jogador == 0 :
        print('O computador GANHOU!!!')
        print('COMPUTADOR: {} X JOGADOR: {}'.format(itens[computador], itens[jogador]))
    if jogador == 1:
        print('DEU EMPATE!!!')
        print('COMPUTADOR: {} X JOGADOR: {}'.format(itens[computador], itens[jogador]))
    if jogador == 2:
        print('Você GANHOU!!!')
        print('COMPUTADOR: {} X JOGADOR: {}'.format(itens[computador], itens[jogador]))
    else:
        print('Jogada INVÁLIDA!')
elif computador == 2 :
    if jogador == 0:
        print('\33[1;30;42m Você GANHOU!!!')
        print('COMPUTADOR: {} X JOGADOR: {}'.format(itens[computador], itens[jogador]))
    if jogador == 1:
        print('Computador GANHOU!!!')
        print('COMPUTADOR: {} X JOGADOR: {}'.format(itens[computador], itens[jogador]))
    if jogador == 2 :
        print('Deu Empate!')
        print('COMPUTADOR: {} X JOGADOR: {}'.format(itens[computador], itens[jogador]))
    else:
        print('Jogada Inválida!')






