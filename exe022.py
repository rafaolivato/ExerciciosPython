nome =str(input('Digite seu nome completo')).strip()

print(' Seu nome com a letra maiúscula é {}'.format(nome.upper()))
print(' Seu nome com a letra minúscula é {}'.format(nome.lower()))
print(' Seu nome tem ao todo {} letras '.format(len(nome) - nome.count(' ')))
print(' Seu primeiro nome tem {} letras'.format(nome.find(' ')))
