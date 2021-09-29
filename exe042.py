a = int(input('\33[1;30;42m Digite a primeira medida do triângulo : \33[m'))
b = int(input('\33[2;30;46m Digite a segunda medida do triângulo : \33[m'))
c = int(input('\33[3;30;47m Digite a terceira medida do triângulo : \33[m'))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b)  < c < (a + b):
    print ('\33[1;32;40m O triângulo pode ser formado, \33[m', end='')
    if a == b == c:
        print('\33[1;30;42m EQUILÁTERO. \33[m')
    elif a != b and a != c and b != c:
        print('\33[1;30;42m ESCALENO.\33[m')
    else:
        print('\33[1m ISÓSCELES')

else:
    print('\33[1;30;41m O triângulo não pode ser formado\33[m')

if a==b and c != a and c != b:
    if a==c and b != a and b!= c:
        if b==c and a != b and  a!= c:
            print('\33[1;30;42m O triângulo é isósceles, tem dois lados iguais\33[m')

