import os

CARPETA = 'contacts/'
EXTENSION = '.txt'

class Contact():

    def __init__(self, name, phone, category, city):
        self.name = name
        self.phone = phone
        self.category = category
        self.city = city

def Contacts():

    #Revisa si la carpeta existe o no
    crear_contact()

    #Muestra el menu
    mostrar_menu()

    #Preguntar la opcion
    pregunta = True

    while pregunta:
        opcion = input('Selecione la opcion \r\n')
        opcion = int(opcion)
        if opcion == 1:
            agregar_contact()
            pregunta = False
        elif opcion == 2:
            update_contact()
            pregunta = False
        elif opcion == 3:
            view_contact()
            pregunta = False
        elif opcion == 4:
            search_contact()
            pregunta = False
        elif opcion == 5:
            delete_contact()
            pregunta = False
        else:
            print('Salio Del Programa')

def delete_contact():
    name = input('Digita El Nombre A Eliminar: \r\n')

    try: 
        os.remove(CARPETA + name + EXTENSION)
        print('\r\n Contacto Eliminado Correctamente')
    except:
        print('No Existe El Contacto')
    Contacts()
    
def search_contact():
    name = input('Digita El Nombre Que Vas A Buscar: \r\n')

    try:
        with open(CARPETA + name + EXTENSION) as contact:
            print('Informacion Del Contacto: \r\n')
            for linea in contact:
                print(linea.rsplit())
            print('\r\n')    
    except IOError:
        print('El contacto No Existe')
        print(IOError)
    Contacts()
   
def view_contact():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        with open(CARPETA + archivo ) as contact:
            for linea in contact:
                # Muestra los contacto
                print(linea.rstrip())
            
            print('\r\n')
    Contacts()

def update_contact():
    print('Digita el nombre que quieres actualizar')
    name_anterior = input('Digita El Nombre Que Quieres Editar: \r\n')

    existe = existe_contact(name_anterior)

    if existe:
        with open(CARPETA + name_anterior + EXTENSION, 'w') as archivo:
            name_contact = input('Digita El Nuevo Nombre Del Contacto: \r\n')
            phone_contact = input('Digita El Nuevo Telefono Del Contacto: \r\n')
            category_contact = input('Digita La Nueva Categoria Del Contacto: \r\n')
            city_contact = input('Digita La Nueva Ciudad Del Contacto: \r\n')

            contact = Contact(name_contact, phone_contact, category_contact, city_contact)

            archivo.write('Nombre: ' + contact.name + '\r')
            archivo.write('Phone: ' + contact.phone + '\r')
            archivo.write('Category: ' + contact.category + '\r')
            archivo.write('City: ' + contact.city + '\r')
        os.rename(CARPETA + name_anterior + EXTENSION, CARPETA + name_contact + EXTENSION)
        print('Contacto Actualizado Correctamente...')
    else:
        print('No Se Encontro El Contacto')
    Contacts()

def agregar_contact():
    print('Agrega los datos solicitados')
    name_contact = input('Nombre del contacto \r\n')

    #Validar si un contacto existe
    # existe = os.path.isfile(CARPETA + name_contact + EXTENSION)
    existe = existe_contact(name_contact)

    if not existe:        
        with open(CARPETA + name_contact + EXTENSION, 'w') as archivo:

            # Se agregan el resto de los campos
            phone_contact = input('Digita el Nuevo Telefono del contacto \r\n')
            category_contact = input('Digita La Nueva Categoria del contacto \r\n')
            city_contact = input('Digita La Nueva Ciudad del contacto \r\n')

            # Se Instancia la clase
            contact = Contact(name_contact, phone_contact, category_contact, city_contact)

            # Se escribe el archivo
            archivo.write('Nombre: '+ contact.name + '\n')
            archivo.write('Phone: '+ contact.phone + '\n')
            archivo.write('Categoria: '+ contact.category + '\n')
            archivo.write('City: '+ contact.city + '\n')

            print('\r\n Contacto creado Correctamente \r\n')
    else:
        print('El Contacto Ya Existe! \r\n')
    Contacts()
    
def mostrar_menu():
    print('Seleccione la opcion que quiera hacer')
    print('1) Agregar Contacto')
    print('2) Editar contacto')
    print('3) Ver contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar contacto')
    print('6) Para salir Del Programa')

def crear_contact():
    if not os.path.exists('contacts/'):
        #Crea la carpeta
        os.makedirs('contacts/')

def existe_contact(name):
    return os.path.isfile(CARPETA + name + EXTENSION)

Contacts()