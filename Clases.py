import pathlib

def concatenar(ruta,i,j):
    ruta = str(pathlib.Path(ruta))
    lista = [ruta,'/', str(i),'/', str(i), '.', str(j)]
    ruta_nueva = ''.join(lista)
    return ruta_nueva #retornamos la ruta

ruta = pathlib.Path(__file__).parent.absolute() # Obtiene el directorio actual
carpetas = int(input("Ingrese el número de carpetas: "))
subcarpetas = int(input("Ingrese el número de subcarpetas: "))

for i in range(1, carpetas + 1):
    archivo = str(pathlib.Path(ruta))
    fullpath = pathlib.Path(archivo + '/' + str(i)).mkdir()
    for j in range(1, subcarpetas + 1):
        pathlib.Path(concatenar(ruta,i,j)).mkdir()
# class Restaurant():

#     def agregar_restaurant(self, name, category, price):
#         self.name = name
#         self.category = category
#         self.price = price
    
#     def mostrar_informacion(self):
#         print(f'Nombre: {self.name}, Category: {self.category}, Price: {self.price}')

# restaurant = Restaurant()
# restaurant.agregar_restaurant('Pizza', 'Americana', 50)
# restaurant.mostrar_informacion()