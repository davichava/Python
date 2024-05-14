#Dictionary simple

# cancion = {
#     'artista' : 'Metalica',
#     'cancion' : 'Web Cam',
#     'lanzamiento' : 2010,
#     'likes' : 4000
# }
# # Acceder alos elementos
# print(cancion['artista'])
# print(cancion['lanzamiento'])

# artista = cancion['artista']
# print(f'Estoy escuchando {artista}')

# ## Agregar Nuevos Valores
# cancion['playlist'] = 'Heavy Metal'
# print(cancion)

# ## Agregar Reemplazar Nuevos Valores
# cancion['cancion'] = 'Seek & Destroy'
# print(cancion)

# ## Eliminar Un Valor
# del cancion['lanzamiento']
# print(cancion)

########Iniciar Dictionary

jugador = {}

print(jugador)

#Se une un jugador
jugador['nombre'] = 'David'
jugador['puntaje'] = 0
print(jugador)

jugador['puntaje'] = 100
print(jugador)

jugador['puntaje'] = 200
print(jugador)

#Acceder a un valor

print(jugador.get('consola', 'No existe ese valor')) 

for clave, valor in jugador.items():
    print(clave)
    print(valor)

del jugador['nombre']
del jugador['puntaje']
print(jugador)