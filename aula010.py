#Condições simples e Compostas

# Condição
# if carro.esquerda():
    #bloco True
# else:
    #bloco False

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 +n2)/2
print('a sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('\33[1;33;41m A sua média foi boa parabéns!!')
else:
    print('\33[2;1;35m A sua média foi ruim. ESTUDE MAIS')