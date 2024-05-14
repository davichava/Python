# peso = float(input('Digite tu peso : '))
# altura = float(input('Digita tu altura : '))

# imc = peso / (altura ** 2)

# if imc < 18.5:
#     resultado = 'Bajo peso'
# elif imc > 25:
#     resultado = 'Sobre Peso'
# else:
#     resultado = 'Normal'

# print(f'Su indice de masa corporas {imc} usted tiene {resultado}')

# masa = int(input('Digita la masa en kilogramo: '))
# #calcular la ecucuon  e=mc^2 mas al cuadrado
# c = 3000000
# energia = masa*c*c

# print('La energia es igual a: ', energia,'Joules')

precio = 50

demonimanaciones = [25, 10, 5]
ingresado = 0 
adeudado = precio

while adeudado > 0:
    moneda = int(input('Ingrese una moneda de (25), (10), (5): '))
    if moneda in demonimanaciones:
        ingresado += moneda
        adeudado -= moneda
        print("Monto adeudado: {} centavos".format(adeudado))
    else:
        print('Moneda No Aceptada. Ingresa una moneda de 25, 10 o 5 centavos')
if ingresado > precio:
    cambio = ingresado - precio
    print("Su Cambio es:  {} entavos".format(cambio))
