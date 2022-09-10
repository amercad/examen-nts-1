cantidadNumero = int( input('Digite la cantidad de numero que desea encontrar: ') )

contMulDos = 0
contMulTres = 0


for i in range(cantidadNumero):
    numero = int( input('Digite un numero: ') )

    if ( numero % 2 == 0):
        contMulDos += 1

    if ( numero % 3 == 0):
        contMulTres += 1


print( f'Los multiplos de dos son: { contMulDos }' )
print( f'Los multiplos de tres son: { contMulTres }' )