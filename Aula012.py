nome = str(input('\33[33m Qual é o seu nome ? '))
if nome == 'Rafael':
    print('Seu nome é bonito')
elif nome =='Pedro' or nome =='Maria'or nome == 'Paulo':
    print ('\33[32m Seu nome é bem popular no Brasil')
elif nome in 'Jessica, ana , jordana , elisangela':
    print ('\33[2;30;47m Sau nome é bem feminino \33[m')
else:
    print(' Seu nome é bem normal')
print('\33[1;30;47m  Tenha um bom dia ! {}\33[m'.format(nome))