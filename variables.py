# book = ('Principito')
# print(book)

# food = ('Rice')
# print(food)


# name = 'David'
# age = 28

# print(name )

# def information():
#     print('I am David')

# information()

# def information(name, profesion):
#     print(f'Soy {name}y soy {profesion}')

# information('David', 'Programador')
# information('Miguel', 'Suboficial')


# def information(name):
#     return name

# empleado = information('David')
# print(empleado)

# name = 'dog'
# def mostrar_nombre(name):
#     print(f'Hola {name}')
# mostrar_nombre(name)

# print(name.upper())
# print(name.title())

# def suma(a=0, b=0):
#     print(a/b)
# suma(2,3)

#List
# lenguajes = ['Python', 'Kotlin','Java', 'Javascripts']

# lenguajes.sort() #Ordenar por elementos
# print(lenguajes)

# print(lenguajes[0])

# #Acceder a un elemento dentro de un texto
# aprendiendo = f'Estoy aprendiendo {lenguajes[0]}'
# print(aprendiendo)

# #Modificar valores de un arreglo

# lenguajes[2] = 'Javascrips'
# print(lenguajes)

# #Agregar elementos a un arreglo

# lenguajes.append('Ruby')
# print(lenguajes)

# # Eliminar De un arreglo
# del lenguajes[1]
# print(lenguajes)

# #eliminar un arreglo

# lenguajes.pop()
# print(lenguajes)

# lenguajes.remove('Java')
# print(lenguajes)

###### Iteradores

lenguajes = ['Python', 'Kotlin','Java', 'Javascripts']

for lenguaje in lenguajes:
    print(f'Estos son los lenguajes {lenguaje}')

# For que escriba numeros

for numero in range(0, 10):
    print(numero)