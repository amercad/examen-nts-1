frutas = []


for i in range(10):
    fruta = {}
    fruta['nombre'] = input('Digite el nombre de la fruta: ')
    fruta['color'] = input('Digite el color de la fruta: ')
    fruta['precio'] = input('Digite el precio de la fruta: ')

    frutas.append( fruta )

    print()


contInverso = len(frutas) 



for i in range(2):
    print(f'FRUTA {i}: { frutas[contInverso - 1] }')
    contInverso -= 1
