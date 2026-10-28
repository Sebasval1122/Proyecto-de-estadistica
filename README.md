# Proyecto-de-estadistica

## Algoritmos de ordenamiento

Un **algoritmo de ordenamiento** toma una lista de elementos y los acomoda en un orden definido, por lo general de menor a mayor. Ordenar datos es un paso previo muy común en estadística: calcular la **mediana**, los **cuartiles**, los **percentiles** o el **rango** exige tener los datos ordenados.

### Conceptos clave

- **Complejidad temporal:** cuántas operaciones hace el algoritmo en función del número de elementos `n`. Se expresa con notación Big-O, por ejemplo `O(n²)` u `O(n log n)`.
- **Complejidad espacial:** cuánta memoria adicional necesita.
- **Estabilidad:** un algoritmo es *estable* si conserva el orden relativo de los elementos con el mismo valor.
- **In-place:** ordena dentro de la misma lista, sin usar una copia de tamaño `n`.

### Comparación

| Algoritmo     | Mejor caso   | Caso promedio | Peor caso    | Memoria extra | Estable |
|---------------|--------------|---------------|--------------|---------------|---------|
| Burbuja       | `O(n)`       | `O(n²)`       | `O(n²)`      | `O(1)`        | Sí      |
| Selección     | `O(n²)`      | `O(n²)`       | `O(n²)`      | `O(1)`        | No      |
| Inserción     | `O(n)`       | `O(n²)`       | `O(n²)`      | `O(1)`        | Sí      |
| Merge Sort    | `O(n log n)` | `O(n log n)`  | `O(n log n)` | `O(n)`        | Sí      |
| Quick Sort    | `O(n log n)` | `O(n log n)`  | `O(n²)`      | `O(log n)`    | No      |
| Heap Sort     | `O(n log n)` | `O(n log n)`  | `O(n log n)` | `O(1)`        | No      |
| Counting Sort | `O(n + k)`   | `O(n + k)`    | `O(n + k)`   | `O(k)`        | Sí      |
| Radix Sort    | `O(d·(n + b))` | `O(d·(n + b))` | `O(d·(n + b))` | `O(n + b)` | Sí      |
| Shell Sort    | `O(n log n)` | depende de los saltos | `O(n²)` | `O(1)`      | No      |

> `k` es el rango de valores posibles (valor máximo − valor mínimo + 1), `d` es la cantidad de dígitos del número más grande y `b` es la base (10 en los ejemplos).

---

### 1. Ordenamiento burbuja (Bubble Sort)

Recorre la lista varias veces y compara elementos vecinos; si están en el orden incorrecto, los intercambia. En cada pasada el mayor elemento "sube" al final, como una burbuja. Si una pasada no hace intercambios, la lista ya está ordenada.

```python
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
```

**Cuándo usarlo:** sobre todo para enseñar; es poco eficiente con listas grandes.

### 2. Ordenamiento por selección (Selection Sort)

Busca el elemento más pequeño de la parte no ordenada y lo coloca al principio. Repite el proceso con el resto de la lista.

```python
def seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista
```

**Cuándo usarlo:** cuando importa hacer pocos intercambios (hace como máximo `n − 1`).

### 3. Ordenamiento por inserción (Insertion Sort)

Construye la lista ordenada de un elemento a la vez: toma cada elemento y lo inserta en su posición correcta dentro de la parte ya ordenada, igual que al ordenar cartas en la mano.

```python
def insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista
```

**Cuándo usarlo:** con listas pequeñas o casi ordenadas, donde es muy rápido.

### 4. Ordenamiento por mezcla (Merge Sort)

Usa la estrategia **divide y vencerás**: divide la lista en dos mitades, ordena cada mitad de forma recursiva y luego las mezcla en una sola lista ordenada.

```python
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
```

**Cuándo usarlo:** cuando se necesita un rendimiento garantizado de `O(n log n)` y estabilidad.

### 5. Ordenamiento rápido (Quick Sort)

También es **divide y vencerás**: elige un elemento llamado **pivote**, coloca a su izquierda los menores y a su derecha los mayores, y repite el proceso en cada lado.

```python
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)
```

> Esta versión es la más fácil de leer, pero crea listas nuevas. La versión *in-place* (particiones de Lomuto o Hoare) usa menos memoria.

**Cuándo usarlo:** es de los más rápidos en la práctica; el peor caso `O(n²)` aparece si el pivote se elige mal de forma repetida.

### 6. Ordenamiento por montículos (Heap Sort)

Convierte la lista en un **montículo máximo** (*max-heap*), un árbol binario donde cada padre es mayor que sus hijos. Luego extrae el máximo, lo pone al final y reconstruye el montículo con el resto.

```python
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
```

**Cuándo usarlo:** cuando se quiere `O(n log n)` garantizado sin memoria extra.

### 7. Ordenamiento por conteo (Counting Sort)

No compara elementos: cuenta cuántas veces aparece cada valor y reconstruye la lista a partir de esos conteos. Es la misma idea que una **tabla de frecuencias** en estadística.

```python
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
```

**Cuándo usarlo:** con números enteros en un rango pequeño (por ejemplo, edades o calificaciones).

### 8. Ordenamiento por residuos (Radix Sort)

Tampoco compara elementos: ordena los números **dígito por dígito**, empezando por las unidades, luego las decenas, luego las centenas, y así sucesivamente. En cada pasada agrupa los números en "cubetas" según el dígito actual, sin cambiar el orden que ya tenían dentro de cada cubeta (por eso el resultado es correcto).

```python
def radix_sort(lista):
    # Esta versión funciona con enteros no negativos.
    if not lista:
        return lista
    exp = 1
    while max(lista) // exp > 0:
        cubetas = [[] for _ in range(10)]
        for x in lista:
            cubetas[(x // exp) % 10].append(x)
        lista = [x for cubeta in cubetas for x in cubeta]
        exp *= 10
    return lista
```

> Para incluir números negativos se ordenan aparte los negativos (por su valor absoluto) y luego se colocan, invertidos, antes de los positivos.

**Cuándo usarlo:** con muchos enteros de pocos dígitos (por ejemplo, códigos postales o números de documento), donde puede superar a los algoritmos `O(n log n)`.

### 9. Ordenamiento Shell (Shell Sort)

Es una mejora del ordenamiento por inserción. En lugar de comparar solo elementos vecinos, compara elementos separados por un **salto** (*gap*) grande y lo va reduciendo hasta llegar a 1. Así los elementos lejanos de su posición se mueven rápido, y la pasada final por inserción encuentra la lista casi ordenada.

```python
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
```

> Su rendimiento depende de la secuencia de saltos. Aquí se usa la original de Shell (`n/2, n/4, …, 1`); otras, como la de Knuth (`1, 4, 13, 40, …`), dan mejores tiempos.

**Cuándo usarlo:** con listas medianas cuando se quiere algo más rápido que inserción sin usar memoria extra ni recursión.

---

### Ejemplo aplicado a estadística

```python
datos = [7, 2, 9, 4, 4, 1, 8, 5]
ordenados = merge_sort(datos)          # [1, 2, 4, 4, 5, 7, 8, 9]

n = len(ordenados)
if n % 2 == 0:
    mediana = (ordenados[n // 2 - 1] + ordenados[n // 2]) / 2
else:
    mediana = ordenados[n // 2]

rango = ordenados[-1] - ordenados[0]

print("Mediana:", mediana)  # 4.5
print("Rango:", rango)      # 8
```

En la práctica, Python ya trae `sorted(lista)` y `lista.sort()`, que usan **Timsort** (una mezcla de Merge Sort e Inserción). Es estable y tiene complejidad `O(n log n)`.

### Cómo ejecutar el código

Todos los algoritmos están en `ordenamiento.py` (solo usa Python 3, sin dependencias).

```bash
python3 ordenamiento.py           # ordena un ejemplo con cada algoritmo y muestra mediana y rango
python3 -m unittest -v            # corre las pruebas de test_ordenamiento.py
```

### Referencias

- Cormen, T. H., Leiserson, C. E., Rivest, R. L. y Stein, C. *Introduction to Algorithms*. MIT Press.
- Documentación de Python: [Sorting Techniques](https://docs.python.org/3/howto/sorting.html).
