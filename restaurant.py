import os

CARPETA = 'restaurant/'
EXTENSION = '.txt'

class Restauran():
    def __init__(self, name, drink, accompany, tip):
        self.name = name
        self.drink = drink
        self.accompany = accompany
        self.tip = tip

def Restaurant():

    #crea la carpeta
    crear_menu()

    #muestra el Menu
    mostrar_menu()

    preguntar = True

    while preguntar:
        opcion = input('Digite La Opcion Que Deseas Hacer: \r\n')
        opcion = int(opcion)
        if opcion == 1:
            add_order()
            preguntar = False
        elif opcion == 2:
            update_order()
            preguntar = False
        elif opcion == 3:
            view_order()
            preguntar = False
        elif opcion == 4:
            searc_order()
            preguntar = False
        elif opcion == 5:
            delete_order()
            preguntar = False
        elif opcion == 6:
            print('Salio Del Programa \r\n')
        else: 
            print('No Entiendo Lo Que Quieres Hacer!!!')

def delete_order():
    name_order = input('Digite La Orden A Eliminar: \r\n')
    try:
        os.remove(CARPETA + name_order + EXTENSION)
        print('Orden Emininada Exitosamente!!!')
    except:
        print('No Existe La Orden...')
    Restaurant()
    
def searc_order():
    name_order = input('Digite La Orden Que Desea Ver \r\n')
    try:
        with open(CARPETA + name_order + EXTENSION) as order:
            print('Informacion De La Orden: \r\n')
            for linea in order:
                print(linea.rsplit())
            print('\r\n')
    except IOError:
        print('Orden No Existe!!!')
        print(IOError)
    Restaurant()
    
def view_order():
    orders = os.listdir(CARPETA)

    orders_txt = [i for i in orders if i.endswith(EXTENSION)]
    for order in orders_txt:
        with open(CARPETA + order) as order:
            for linea in order:
                # Muestra las ordenes
                print(linea.rsplit())

            print('\r\n')
    Restaurant()
    
def update_order():
    print('Desde agregar')
    name_former = input('Digital El Nombre Que Quieras Editar: \r\n')

    existe = existe_order(name_former)
    if existe:
        with open(CARPETA + name_former + EXTENSION, 'w') as restaurant:
            name_order = input('Digita Orden Nueva: \r\n')
            drink_order = input('Digita La Bebida Nueva : \r\n')
            accompany_order = input('Ditiga El acompañante Nuevo: \r\n')
            tip_order = input('Digita La Propina Nueva: \r\n')

            restauran = Restauran(name_order, drink_order, accompany_order, tip_order)

            restaurant.write('Nombre: ' + restauran.name + '\n')
            restaurant.write('Tomar: ' + restauran.drink + '\n')
            restaurant.write('Acompañante: ' + restauran.accompany + '\n')
            restaurant.write('Propina: ' + restauran.tip + '\n')
            print('Orden Actualizada...')
        os.rename(CARPETA + name_former + EXTENSION, CARPETA + name_order + EXTENSION)
    else:
        print('Plato No Existe...')
    Restaurant()

def add_order():
    name_plate = input('Agrega Tu Plato Al Menu: \r\n')
    existe = existe_order(name_plate)
    # existe = os.path.isfile(CARPETA + name_plate + EXTENSION)
    
    if not existe:
        with open(CARPETA + name_plate + EXTENSION, 'w') as restaurant:

            drink_restaurant = input('Que Deseas Tomar \r\n')
            accompany_restaurant = input('Desea Un Acompañante \r\n')
            tip_restaurant = input('Desea Agregar Propina \r\n')

            restauran = Restauran(name_plate, drink_restaurant, accompany_restaurant, tip_restaurant)

            restaurant.write('Nombre: '+ restauran.name + '\n')
            restaurant.write('Tomar: ' + restauran.drink + '\n')
            restaurant.write('Acompañante: '+ restauran.accompany + '\n')
            restaurant.write('Propina: '+ restauran.tip + '\n')

            print('Plato Guardo Correcamente... \r\n')
    else:
        print('El Plato Ya lo Pedistes!!! \r\n')
    Restaurant()

def mostrar_menu():
    print('Seleccione La Opcion Que Desees: \r\n')
    print('1) Agregar pedido: ')
    print('2) Editar pedido: ')
    print('3) Ver pedido: ')
    print('4) Buscar pedido: ')
    print('5) Eliminar pedido: ')
    print('6) Salir Del Programa: ')

def crear_menu():
    if not os.path.exists('restaurant/'):
    #Crea la carpeta
        os.makedirs('restaurant/')

def existe_order(name):
    return os.path.isfile(CARPETA + name + EXTENSION)

Restaurant()
