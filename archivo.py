# def app():
#     ## se crea el archivo.
#     archivo = open('archivo.txt', 'w') # Es un archivo de escritura
#     for i in range(0, 20):
#         archivo.write('Esta es la linea' + str(i) + '\r\n')

#     archivo.close()

# app()


# def app():

#     with open('archivo.txt') as archivo:
#         for contenido in archivo:
#             print(contenido.rstrip()) ## rstrip es para eliminar los saltos de linea

# app()

import requests
# Realizar una solicitud GET a una API

response = requests.get('https://api.example.com/data')

# Obtener los datos de la respuesta
data = response.json()

# Mostrar los datos
print(data)

