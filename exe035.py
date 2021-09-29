a = int(input('\33[1;30;42m Digite a primeira medida do triângulo : \33[m'))
b = int(input('\33[2;30;46m Digite a segunda medida do triângulo : \33[m'))
c = int(input('\33[3;30;47m Digite a terceira medida do triângulo : \33[m'))

if (b - c) < a < (b + c):
    if (a - c) < b < (a + c):
        if (a - b)  < c < (a + b):
            print ('\33[1;32;40m O triângulo pode ser formado\33[m')
else:
    print('\33[1;30;41m O triângulo não pode ser formado\33[m')