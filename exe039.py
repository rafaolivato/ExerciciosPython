idade = int(input('\33[1;43m Qual é a sua idade ?\33[m  ' ))
if idade > 18:
    velho = idade - 18

    print('\33[1;30;45mVocê já passou {} anos da idade do listamento, AGILIZE O PROCESSO !!!''\33[31m'.format(velho))
if idade == 18:
    print('\33[1;2;3;4;30;44m Você precisa se alistar urgente !!!\33[m')
if idade < 18:
    jovem = 18 - idade
    print('\33[1;30;42m Você ainda é muito jovem para se alistar, falta {} anos.\33[m '.format(jovem))