
# RETOS

# def welcome(house, name):
#     print(f'Bienvenido A {house} {name}')
# welcome('Casa', 'David')

# def welcome1(name):
#     return name
# people = welcome1('David')
# print(people)

# name = 'David'
# def welcome2(name):
#     print(f'Welcome {name}')
# welcome2(name.upper())
# print(name.upper())


#### Reto Entrada de Datos

# pregunta1 = input('Tienes 18 años \r\n')
# pregunta2 = input('Estas Estudiando \r\n')
# pregunta3 = input('Ya te graduastes \r\n')


# calificacion = 0

# if pregunta1.lower() == 'si':
#     calificacion += 1
#     print(f'Tuiene un punto extra. Turespuesta fue {pregunta1}')
# elif pregunta2.lower() == 'si':
#     calificacion += 1
#     print(f'Tuiene un punto extra. Turespuesta fue {pregunta2}')
# elif pregunta3.lower() == 'si':
#     calificacion += 1
#     print(f'Tuiene un punto extra. Tu respuesta fue {pregunta3}')
# else:
#     print(f'Tu calificacion fue {calificacion}')

pregunta1 = input('Tienes 18 años \r\n')
pregunta2 = input('Estás Estudiando \r\n')
pregunta3 = input('Ya te graduaste \r\n')

calificacion = 0

if pregunta1 == 'si':
    calificacion += 1
    print(f'Tienes 1 punto extra. Tu respuesta fue {pregunta1}')
if pregunta2 == 'si':
    calificacion += 1
    print(f'Tienes 1 punto extra. Tu respuesta fue {pregunta2}')
if pregunta3 == 'si':
    calificacion += 1
    print(f'Tienes 1 punto extra. Tu respuesta fue {pregunta3}')

    print(f'Tu calificación fue {calificacion}')