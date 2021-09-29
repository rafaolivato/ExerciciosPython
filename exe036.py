casa = float(input('\33[30;47m Qual o valor da casa que desejas? \33[m'))
salario = int(input('\33[30;47m Qual é o seu salário ? \33[m'))
anos = int(input('\33[30;47m Quantos anos pretende pagar a casa ?\33[m'))
prestacao = casa / (anos*12)
print (' A prestação será de {}'.format(prestacao))
if prestacao > salario / 3:
    print('     \33[7;1;31;47m Seu empréstimo foi negado\33[m')
else:
    print ('    \33[3;30;47m Seu empréstimo foi aprovado\33[m')
