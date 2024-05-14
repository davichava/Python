# def linear_search(lista, elemento):
#     for i in range(len(lista)):
#         if lista[1] == elemento:
#             return i
#     return -1

# numeros = [64, 34, 25, 12, 22, 11, 90]
# elemento_buscado = 22
# indice = linear_search(numeros, elemento_buscado)
# if indice != -1:
#     print(f"El elemento {elemento_buscado} se encuentra en el {indice}")
# else:
#     print(f"El elemento {elemento_buscado} No se Encuentra en la lista")



######BUBLEE SORT

# def bublle_sort(lista):
#     n = len(lista)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if lista[j] > lista[j + 1]:
#                 lista [j], lista[j+1] = lista[j+1], lista[j]

# numeros = [64, 34, 25, 12, 22, 11, 90]
# bublle_sort(numeros)
# print(numeros)


##########INSERT _SORT
# def insertion_sort(lista):
#     for i in range(1, len(lista)):
#         key = lista[i]
#         j = i - 1
#         while j >= 0 and key < lista[j]:
#             lista[ j+ 1 ] = lista[j]
#             j -= 1
#         lista[j + 1] = key

# numeros = [64, 34, 25, 12, 22, 11, 90]
# insertion_sort(numeros)
# print(numeros)


###### SELECTION_SORT
# def selection_sort(lista):
#     n = len(lista)
#     for i in range(n):
#         indice_minimo = i
#         for j in range(i + 1, n):
#             if lista [j] < lista[indice_minimo]:
#                 indice_minimo = j
#         lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
# numeros = [64, 34, 25, 12, 22, 11, 90]
# selection_sort(numeros)
# print(numeros)

import random

numeros = [random.randint(1, 100) for _ in range(20)]
print(f'Lista desornedanda: {numeros}')

def bublle_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j + 1]:
                lista [j], lista[j+1] = lista[j+1], lista[j]
bublle_sort(numeros)
print(f'Lista ordenada {numeros}')