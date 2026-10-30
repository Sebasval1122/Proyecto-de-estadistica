"""Algoritmos de ordenamiento descritos en el README.

burbuja ordena la lista recibida (in-place) y la devuelve; merge_sort y
quick_sort devuelven una lista nueva.
"""


def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            break
    return lista


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)


ALGORITMOS = [burbuja, merge_sort, quick_sort]


def mediana(datos):
    ordenados = merge_sort(list(datos))
    n = len(ordenados)
    if n % 2 == 0:
        return (ordenados[n // 2 - 1] + ordenados[n // 2]) / 2
    return ordenados[n // 2]


def rango(datos):
    ordenados = merge_sort(list(datos))
    return ordenados[-1] - ordenados[0]


if __name__ == "__main__":
    datos = [7, 2, 9, 4, 4, 1, 8, 5]
    print("Datos:", datos)
    for algoritmo in ALGORITMOS:
        print(f"{algoritmo.__name__:>14}:", algoritmo(list(datos)))
    print("Mediana:", mediana(datos))
    print("Rango:", rango(datos))
