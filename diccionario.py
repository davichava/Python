#######DICCIONARIOS

# puntajes = {'Juan':95, 'Maria': 87, 'David': 29, 'Ana': 92 }

# print(puntajes['David'])

# puntajes['David'] = 30
# print(puntajes)

# #Agregar
# puntajes['carlos'] = 2
# print(puntajes)

# #Eliminar
# del puntajes['Ana']
# print(puntajes)

############CANCIONES MUSICA

musica = [('Ella Se Contradice', 'Farruco', 3.5),
        ('Cuando Me Diras', 'Nicky', 7.9),
        ('LLegamos Ala Disco', 'Arcangel', 10.0),
        ('Por Amar A Ciegas', 'Arcangel', 100)]

def buscar_cancion(nombre):
    for cancion in musica:
        if cancion[0] == nombre:
            return cancion
    return None

def buscar_artista(artista):
    canciones_artista = []
    for cancion in musica:
        if artista[1] == artista:
            canciones_artista.append(cancion)
    return canciones_artista

print(buscar_cancion('Por Amar A Ciegas'))
print(buscar_cancion('LLegamos Ala Disco'))
print(buscar_artista('Arcangel'))