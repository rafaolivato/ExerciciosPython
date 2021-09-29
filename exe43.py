peso = float(input('Qual é o seu peso ? '))
altura = float(input('Qual é o sua altura (em metros) ? '))

imc = peso/altura**2
print (' Seu imc é {:.2f}' .format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <25:
    print('Peso ideal')
elif 25 <= imc <30:
    print('Sobrepeso')
elif 30<= imc < 40:
    print('Obeso')
elif imc >= 40:
    print('Obesidade mórbida')
