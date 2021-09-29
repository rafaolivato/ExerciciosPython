nota1 = float(input('\33[1;30;47m Digite a primeira nota entre 0 e 10: \33[m'))
nota2 = float(input('\33[1;30;42m Digite a segunda nota entre 0 e 10: \33[m'))
media = (nota1 + nota2) / 2
if media < 5:
    print('\33[1;30;43m Você foi reprovado, nota final: {} \33[m'.format(media))
if 5 <= media < 6.9:
    print('\33[1;30;41m Você está de recuperação, nota final:  {} \33[m'.format(media))
if media >= 7:
    print('\33[1;30;42m Você foi aprovado !!!, nota final: {}  \33[m'.format(media))