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
| Merge Sort    | `O(n log n)` | `O(n log n)`  | `O(n log n)` | `O(n)`        | Sí      |
| Quick Sort    | `O(n log n)` | `O(n log n)`  | `O(n²)`      | `O(log n)`    | No      |

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

### 2. Ordenamiento por mezcla (Merge Sort)

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

### 3. Ordenamiento rápido (Quick Sort)

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

En la práctica, Python ya trae `sorted(lista)` y `lista.sort()`, que usan **Timsort** (una mezcla de Merge Sort y ordenamiento por inserción). Es estable y tiene complejidad `O(n log n)`.

### Cómo ejecutar el código

Los tres algoritmos están en `ordenamiento.py` (solo usa Python 3, sin dependencias).

```bash
python3 ordenamiento.py           # ordena un ejemplo con cada algoritmo y muestra mediana y rango
python3 -m unittest -v            # corre las pruebas de test_ordenamiento.py
python3 benchmark.py              # mide 100 veces cada algoritmo por tamaño y regenera los datos
```

### Estudio estadístico

`index.html` presenta el estudio completo: planteamiento del problema, recolección de datos, análisis (estadística descriptiva y pruebas de hipótesis) y conclusiones. Se abre directamente en el navegador; los datos ya vienen incluidos.

Los datos medidos están en `datos/mediciones.json` y `datos/mediciones.csv` (una fila por medición: algoritmo, tamaño `n`, número de repetición y tiempo en milisegundos).

### Referencias

- Cormen, T. H., Leiserson, C. E., Rivest, R. L. y Stein, C. *Introduction to Algorithms*. MIT Press.
- Documentación de Python: [Sorting Techniques](https://docs.python.org/3/howto/sorting.html).
