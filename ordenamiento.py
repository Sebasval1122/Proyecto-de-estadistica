"""Algoritmos de ordenamiento descritos en el README.

Las funciones burbuja, seleccion, insercion, heap_sort y shell_sort ordenan
la lista recibida (in-place) y la devuelven; las demás devuelven una lista nueva.
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


def seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista


def insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
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


def heap_sort(lista):
    def hundir(lista, n, i):
        mayor = i
        izq, der = 2 * i + 1, 2 * i + 2
        if izq < n and lista[izq] > lista[mayor]:
            mayor = izq
        if der < n and lista[der] > lista[mayor]:
            mayor = der
        if mayor != i:
            lista[i], lista[mayor] = lista[mayor], lista[i]
            hundir(lista, n, mayor)

    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        hundir(lista, n, i)
    for fin in range(n - 1, 0, -1):
        lista[0], lista[fin] = lista[fin], lista[0]
        hundir(lista, fin, 0)
    return lista


def counting_sort(lista):
    if not lista:
        return lista
    minimo, maximo = min(lista), max(lista)
    conteo = [0] * (maximo - minimo + 1)
    for x in lista:
        conteo[x - minimo] += 1
    resultado = []
    for valor, veces in enumerate(conteo):
        resultado.extend([valor + minimo] * veces)
    return resultado


def radix_sort(lista):
    if not lista:
        return lista
    if min(lista) < 0:
        raise ValueError("radix_sort solo acepta enteros no negativos")
    exp = 1
    while max(lista) // exp > 0:
        cubetas = [[] for _ in range(10)]
        for x in lista:
            cubetas[(x // exp) % 10].append(x)
        lista = [x for cubeta in cubetas for x in cubeta]
        exp *= 10
    return lista


def shell_sort(lista):
    salto = len(lista) // 2
    while salto > 0:
        for i in range(salto, len(lista)):
            actual = lista[i]
            j = i
            while j >= salto and lista[j - salto] > actual:
                lista[j] = lista[j - salto]
                j -= salto
            lista[j] = actual
        salto //= 2
    return lista


ALGORITMOS = [burbuja, seleccion, insercion, merge_sort, quick_sort,
              heap_sort, counting_sort, radix_sort, shell_sort]


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
