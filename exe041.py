idade = int(input('\33[1;30;42m Qual é a sua idade ? \33[m'))
if idade <= 9:
    print ('Sua categoria é mirim, você tem {} anos'.format(idade))
elif idade <= 14:
    print('\33[1;30;43m Sua categoria é infantil, você tem {} anos'.format(idade))
elif idade <= 19:
    print('\33[1;30;44m Sua categoria é junior, você tem {} anos'.format(idade))
elif idade <= 20:
    print ('\33[1;30;45m Sua categoria é sênior, você tem {} anos'.format(idade))
else:
    print ('\33[1;30;46m Sua categoria é master, você tem {}'.format(idade))
