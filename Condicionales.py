# balance = 500

# if balance == 500:
#     print('Puedes pagar')
# elif balance < 200:
#     print('No puedes pagar')
    
# usuario_autenticado = True

# if usuario_autenticado:
#     print('Acceso exitoso')
# else:
#     ('Debes iniciar sesion')

# lenguajes = ['Python', 'Kotlin','Java', 'Javascripts']

# if 'Ruby' in lenguajes:
#     print('Python Existe')
# else:
#     print('No no esta en la lista')

# IF anidados
usuario_autenticado = False
# usuario_admin = False

# if usuario_autenticado:
#     if usuario_admin:
#         print('Acceso Total')
#     else:
#         print('Acceso Al Sistema')
# else:
#     print('Debes iniciar sesion')


# ocupacion = 'estudiante'
# matricula = 101000

# # if ocupacion == 'estudiante' and ocupacion == 'Jubilado':
# if ocupacion == 'estudiante':
#     print(f'Tienen es 50% de descueto')
# elif ocupacion == 'jubilado':
#     print('Tiene un 75% de descuento')
# else:
#     print('Tienes que pagar el 100%')



######## AND OR

# usuario_logueado = True
# usuario_admin = False

# # if usuario_logueado or usuario_admin:
# if usuario_logueado and usuario_admin:
#     print('Administrador')
# elif usuario_logueado:
#     print('No tienes privelegios de Administrador')
# else:
#     print('Debes Iniciar sesion')


#########

lenguajes = ['Python', 'Kotlin','Java', 'Javascripts']

for lenguaje in lenguajes:
    if lenguaje == 'Python':
        print(lenguaje.upper())
    else:
        print(lenguaje)