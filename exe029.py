vel = int(input('Velocidade medida pelo radar:  '))
if vel > 80:
    print(' Você receberá em breve uma multa de R$ ', (vel * 7) - 560)