# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# numero = 5
# resultado = factorial(numero)
# print(f' El factorial de {numero} es: {resultado} ')

def perturbaciones(lista):
    if len(lista) == 0:
        return []
    if len(lista) == 1:
        return[lista]
    l = []
    for i in range(len(lista)):
        m = lista[i]
        lista_remanente = lista[:i] + lista[i+1:]
        for p in perturbaciones(lista_remanente):
            l.append([m] + p)
    return l
## devuelve todas las posibles convinaciones de estos numeros
numeros = [1, 2, 3]
print(perturbaciones(numeros))