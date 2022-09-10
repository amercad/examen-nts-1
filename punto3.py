print("***MENU***")
print("Digitar 1 para recibir un producto")
print("Digitar 2 para mostrar todos los productos registrados")
print("Digitar 3 para editar el precio producto")
print("Digitar 4 para eliminar el producto")
print("Digitar 5 para SALIR")

productos=[]

opt = 100

while( opt != 5 ):

    opt = int( input('Digite la opcion elegida: ') )

    producto = {}

    if (opt == 1):
        producto['codigo'] = int(input('Digite el codigo del producto: '))
        producto['nombre'] = input('Digite el nombre del producto: ')
        producto['precio'] = float(input('Digite el precio del producto: '))
        productos.append( producto )

    elif( opt == 2 ):
        print(productos)
    elif (opt == 3):
        codigo = int( input('Digite el codigo del producto que desee buscar: ') )
    
        for prod in productos:
            if ( prod['codigo'] == codigo ):
                prod['precio'] = float( input('Digite el nuevo precio: ') )
                break
            else:
                print('Producto no encontrado')
    elif (opt == 4):
        codigo = int( input('Digite el codigo del producto que desee buscar: ') )
    
        for prod in productos:
            if ( prod['codigo'] == codigo ):
               productos.remove(prod)
               print('Producto eliminado')
               break
            else:
                print('Producto no encontrado')
    else:
        print("digite una opcion valida")