playlist = {} # Diccionario vacio
playlist['canciones'] = [] #lista vacia de canciones

def app():
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('Como deseas nombrar tu cancion?\r\n')
        if  nombre_playlist:
            playlist['nombre'] = nombre_playlist
            
            agregar_playlist = False

            print(playlist)

            agregar_canciones()

def agregar_canciones():
    agregar_cancion = True

    while agregar_cancion:
        # PRegunta al usuario que cancion quiere agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\n Agrega el nombre de otra cancion {nombre_playlist}: \r\n'
        pregunta += 'Excribe "X" para cerrar el programa \r\n'

        cancion = input(pregunta)

        if cancion == 'X':
            #Dejar de agregar canciones
            agregar_cancion = False

            #Mostrar resumen de laplaylist
            mostrar_resumen()    
        else:
            #Agregar las canciones a la playlist
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'playlist {nombre_playlist} \r\n')
    print('Canciones:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)   



app()