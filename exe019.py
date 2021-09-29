from random import choice

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
