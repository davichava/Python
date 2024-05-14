import os
CARPETA = 'contactos/'
EXTENSION = '.txt'


class Contactos():
    def __init__(self, nombre, telefono, categoria, ciudad):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
        self.ciudad = ciudad


def App():

    #crear la carpeta de contactos
    crear_contacto()

    #Mostar menu
    crear_menu()

    preguntar = True

    while preguntar:
        opcion = input('Elija una Opcion Valida \r\n')
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            ver_contacto()
            preguntar = False
        elif opcion == 3:
            buscar_contacto()
            preguntar = False
        elif opcion == 4:
            editar_contacto()
            preguntar = False 
        elif opcion == 5:
            elimar_contacto()
            preguntar = False
        elif opcion == 6:
            print('Salistes del Programa...')
            preguntar = False
        else:
            print('No Entiendo Lo Que Haces... \r\n')

def agregar_contacto():
    print('Digite los Campos Solicitados \r\n')
    nombre_contacto = input('Digite el nombre del Contacto \r\n')

    with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

        telefono_contacto = input('Digite el telefono del contacto \r\n')
        categoria_contacto = input('Digite la categoria del contacto \r\n')
        ciudad_contacto = input('Digite la ciudad del contacto \r\n')

        contacto = Contactos(nombre_contacto, telefono_contacto, categoria_contacto, ciudad_contacto)

        archivo.write('Nombre: '+ contacto.nombre + '\n')
        archivo.write('Telefono: '+ contacto.telefono + '\n')
        archivo.write('Categoria: '+ contacto.categoria + '\n')
        archivo.write('Ciudad: '+ contacto.ciudad + '\n')

        print('Contacto Guardad Exitosamente...')

def ver_contacto():
    print('Ver Contacto')


def buscar_contacto():
    print('Buscando Contacto')

def editar_contacto():
    print('Edtando Contacto')

def elimar_contacto():
    print('Elimar Contacto')


def crear_menu():
    print('Seleccione una opcion')
    print('1) Agregar Contactos')
    print('2) Ver Contactos')
    print('3) Buscar Contactos')
    print('4) Editar Contactos')
    print('5) Eliminar Contactos')
    print('6) Salir del Programa')



def crear_contacto():
    if not os.path.exists('contactos/'):
        os.makedirs('contactos/')

App()