import os
import pathlib

CARPETA = 'Company/'
EXTENSION = '.txt'

class Companys():
    def __init__(self, name, represent, location, contact):
        self.name = name
        self.represent = represent
        self.location = location
        self.contact = contact

def Company():
    mostrar_menu()

    # crear_empresa()


    pregunta = True
    
    while pregunta:
        opcion = input('Ingresa la opcion que deseas:  \r\n')
        opcion = int(opcion)

        if opcion == 1:
            add_company()
            pregunta = False
        elif opcion == 2:
            view_company()
            pregunta = False
        elif opcion == 3:
            search_company()
            pregunta = False
        elif opcion == 4:
            update_company()
            pregunta = False
        elif opcion == 5:
            delete_company()
        elif opcion == 6:
            print('Salistes Del Programa...')
        else:
            print('No Entiendo Lo Que Quieres Hacer!!!')

def delete_company():
    name_company = input('Ingresa La Empresa Para Eliminar: \r\n')
    try:
        os.remove(CARPETA + name_company + EXTENSION)
        print('\r\n Empresa Eliminada Correctamente...')
    except:
        print('La empresa No Existe')
    Company()

def update_company():
    print('Digita La Empresa A Editar')
    name_front = input('Digite La empresa Para Modificar: \r\n')
    existe = existe_company(name_front)
    if existe:
        with open(CARPETA + name_front + EXTENSION, 'w') as company:
            name_company = input('Digite El Nuevo Nombre De La Empresa: \r\n')
            represent_company = input('Digita El Nuevo Representante De La Empresa: \r\n')
            location_company = input('Digit La Nueva Ubicacion De La Empresa: \r\n')
            contact_company = int(input('Digite El Nuevo Contacto De La Empresa: \r\n'))

            date = Companys(name_company, represent_company, location_company, contact_company)

            company.write('Nombre: ' + date.name + '\n')
            company.write('Representante: ' + date.represent + '\n')
            company.write('Ubicacion: '+ date.location + '\n')
            company.write('Contacto: ' + date.contact + '\n')
            print('Empresa Editada Correctamente...')
        os.rename(CARPETA + name_front + EXTENSION, CARPETA + name_company + EXTENSION)        
    else:
        print('La Empresa No Existe!!!')
    Company()

def search_company():
    print('Digita La Empresa Que Quieres Buscar')

def view_company():
    archivos = os.listdir(CARPETA)

    archivo_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivos in archivo_txt:
        with open(CARPETA + archivos) as contact:
            for linea in contact:
                print(linea.rsplit())
            print('\r\n')
    Company()           

def add_company():
    name_company = input('Digita El Nombre De la Empresa: \r\n')
    # Ruta Para Ver Si existe
    # existe = os.path.isfile(CARPETA + name_company + EXTENSION)

    existe = existe_company(name_company)

    if not existe:
        with open(CARPETA + name_company + EXTENSION, 'w') as company:
            represent_company = input('Digita El Representate De La Empresa: \r\n')
            location_company = input('Digita La Ubicacion De La Empresa: \r\n')
            Contact_company = input('Digita El Contacto De La Empresa: \r\n')

            date = Companys(name_company, represent_company,  location_company, Contact_company)

            company.write('Nombre Empresa: ' + date.name + '\n')
            company.write('Representate Empresa: ' + date.represent + '\n')
            company.write('Ubicacion Empresa' + date.location + '\n')
            company.write('Contacto Empresa' + date.contact + '\n')
            print('Empresa Guardada Correctamente...')
    else:
        print('La Empresa Ya Existe... \r\n')
    Company()

def mostrar_menu():
    print('Selecciona La Opcion Que Deseas: ')
    print('1) Agregar La Empresa')
    print('2) Ver La Empresa')
    print('3) Buscar La Empresa')
    print('4) Editar La Empresa')
    print('5) Eliminar La Empresa')
    print('6) Salir Del Programa')

# def crear_empresa():
#     if not os.path.exists('Company/'):
#         os.makedirs('Company/')

def existe_company(name):
    return os.path.isfile(CARPETA + name + EXTENSION)


def concatenar(ruta, i, j):
    ruta = str(pathlib.Path(ruta))
    lista = [ruta, '/', str(i), '/', str(i), '.', str(j)]
    ruta_nueva = ''.join(lista)
    return ruta_nueva # retornamos la ruta

ruta = pathlib.Path(__file__).parent.absolute() # Obtiene el directorio actual
nombre_carpeta_principal = input("Ingrese el nombre de la carpeta principal: ")

carpeta_principal = ruta / nombre_carpeta_principal
carpeta_principal.mkdir(parents=True, exist_ok=True) # Crea la carpeta principal si no existe
carpetas = 0
if not next(carpeta_principal.iterdir(), None):  # Comprueba si la carpeta principal está vacía
    carpetas = int(input(f"Ingrese el número de carpetas para '{nombre_carpeta_principal}': "))

    nombre_subcarpeta1 = input("Ingrese el nombre de la primera subcarpeta: ")
    nombre_subcarpeta2 = input("Ingrese el nombre de la segunda subcarpeta: ")

    for i in range(1, carpetas + 1):
        carpeta_actual1 = carpeta_principal / f"{nombre_subcarpeta1}"
        carpeta_actual2 = carpeta_principal / f"{nombre_subcarpeta2}"
        carpeta_actual1.mkdir(parents=True, exist_ok=True) # Crea la primera subcarpeta
        carpeta_actual2.mkdir(parents=True, exist_ok=True) # Crea la segunda subcarpeta
Company()