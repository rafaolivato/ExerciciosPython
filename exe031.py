km = float(input(' Quantos kilometros tem até o seu destino '))
if km <=200:
    print(' O valor da sua viagem custará R$ ', (km * 0.50))
if km > 200:
    print ('O valor da sua viagem custará R$ ', (km * 0.45))