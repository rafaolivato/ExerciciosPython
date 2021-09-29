preco = float(input('\33[1mPreço do produto : '))
dinheiro = preco -(preco * .10)
cartao = preco -(preco * .05)
duasvezes = preco
tresvezes = preco + (preco * .20)
opcao = 0
while opcao != 5:

    print( '''      [1] Dinheiro ou Cheque
      [2] Á vista no cartão
      [3] Parcelado em duas vezes
      [4] Parcelado em três vezes
      [5] Finaliza venda'''
           )
    opcao = int(input('>>>>> Qual é a sua opção ?'))
    print('Volte sempre')

    if opcao == 1:
        print('R$ {}0'.format(dinheiro))
    elif opcao == 2:
        print('R${}0'.format(cartao))
    elif opcao ==3:
        print('R${}0'.format(duasvezes))
    elif opcao ==4:
        print ('R${}0'.format(tresvezes))
    elif opcao ==5:
        print('Finalizando')
    else:
        print('Opção inválida.')

