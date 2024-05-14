def main():

    shoping_list = []

    print('\n ---Escoge la Opcion Correcta---')
    print('1) Agregar Producto')
    print('2) Ver Productos')
    print('3) Eliminar producto')
    print('4) Salir Programa')

    while True:
        option = input('Seleciona Lo Que Quieras Hacer: \r\n')

        if option == '1':
            item = input('Digita El Nombre Del Producto: \r\n')
            shoping_list.append(item)
            print('Producto Agregado')
        elif option == '2':
            print('Estos Son Tus Productos')
            for item in shoping_list:
                print("- " + item)
        elif option == '3':
            item = input('Digita El Nombre Del Producto A Eliminar: \r\n')
            if item in shoping_list:
                shoping_list.remove(item)
            print('Producto Eliminado...')
        elif option == '4':
            break
        else:
            print('No entiendo L')
if __name__ == '__main__':
    main()
