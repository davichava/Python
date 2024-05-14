## DICCIONARIO

inventario = {'manzanas': 10, 'Bananas': 5, 'Naranjas': 3, 'Peras': 7}

def gestionar_inventario(accion, articulo, cantidad=0):
    if accion == 'agregar':
        if articulo in inventario:
            inventario[articulo] += cantidad
        else:
            inventario[articulo] = cantidad
    elif accion == 'quitar':
        if articulo in inventario and inventario[articulo] >= cantidad:
            inventario[articulo] -= cantidad
        else:
            print('No se Realizo La Accion')
    elif accion == 'buscar':
        if articulo in inventario:
            return inventario[articulo]
        else:
            return None
    else:
        print('Accion No Reconocida...')

gestionar_inventario('agregar', 'manzanas', 5)
print(inventario)

gestionar_inventario('quitar', 'naranjas', 2)
print(inventario)

print(gestionar_inventario('buscar', 'peras'))