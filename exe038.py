num1 = int(input('\33[2;47m Digite um número : \33[m'))
num2 = int(input('\33[1;33;47m Digite um outro número : \33[m'))

if num1 > num2:
    print('\33[1;30;47m O primeiro é maior que o segundo\33[m')
if num2 > num1:
    print('\33[2;47m O segundo valor é maior\33[m')
if num1 == num2:
    print('\33[2;32m Os dois números são iguais\33[m')
