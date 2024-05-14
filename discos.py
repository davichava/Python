discos = [
        {'nombre': 'Abbey', 'artista': 'The Beatles', 'Canciones':[('Come Together', 260), ('Something', 182), ('octopues'), 167], 'Stock': 5},
        {'nombre': 'Imagene', 'artista': 'John Lennon', 'Canciones':[('Imagine', 181), ('Crippled', 231), ('It´s so Hard'), 122], 'Stock': 3},            
]

def buscar_disco(discos, nombre=None, artista=None):
    resultado = []
    for disco in discos:
        if nombre and disco['nombre'] == nombre:
            resultado.append(disco)
        if artista and disco['artista'] == artista:
            resultado.append(disco)
    return resultado

def buscar_cancion(discos, nombre):
    resultado = []
    for disco in discos:
        for cancion in disco["Canciones"]:
            if cancion[0] == nombre:
                resultado.append((cancion, disco['nombre'], disco['artista']))
    return resultado

def comprar_disco(discos, nombre):
    for disco in discos:
        if disco['nombre'] == nombre and disco['Stock'] > 0:
            disco['stock'] -= 1
            print(f' Haz comprado {nombre}. Quedan {disco["Stock"]} en stock')
            return
    print(f'No se pudo completar la venta de {nombre}')

##Discos ordenados por nombre

def bubble_sort_discos(discos):
    n = len(discos)
    for i in range(n):
        for j in range(0, n-i-1):
            if discos[j]['nombre'] > discos[j+1]['nombre']:
                discos[j], discos[j+1] = discos[j+1], discos[j]

def buscar_disco_parcial(discos, nombe_parcial, indice=0):
    if indice == len(discos):
        return None
    if nombe_parcial in discos[indice]['nombre']:
        return discos[indice]
    return buscar_disco_parcial(discos, nombe_parcial, indice+1)

print(buscar_disco(discos, nombre='Imagine'))
print(buscar_cancion(discos, "Come Together"))
comprar_disco(discos, 'Imagine')