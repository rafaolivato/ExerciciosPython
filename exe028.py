import random
gerado = random.randint(1, 5)

print ('O computador está pensando em um número entre 1 e 5')

num = int(input('Adivinhe qual número o computador está pensando entre 1 e 5:  '))
if num == gerado:
    print ('Você acertou o número. SENSACIONAL !!!!')
else:
    print (' Não foi desta vez')

    print("Número aleatório gerado:", random.randint(1,5))


