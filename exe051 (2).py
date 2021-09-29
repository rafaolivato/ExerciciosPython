n = int(input('Digite o primeiro termo da PA : '))
# razao é a diferença entre dois termos
r = int(input('Razão: '))
decimo = n +(10-1) * r
for c in range (n,decimo + r,r):

    print ('{} '.format(c), end='->')
print('FIM')