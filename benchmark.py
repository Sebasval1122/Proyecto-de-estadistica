"""Mide 100 veces QuickSort, MergeSort y BubbleSort para varios tamaños de entrada.

Genera datos/mediciones.json, datos/mediciones.csv y embebe el JSON en index.html.
Con --solo-html solo vuelve a embeber el JSON existente en index.html.
"""
import csv
import gc
import json
import platform
import random
import sys
import time
from datetime import datetime, timezone

from ordenamiento import burbuja, merge_sort, quick_sort

ALGORITMOS = {"QuickSort": quick_sort, "MergeSort": merge_sort, "BubbleSort": burbuja}
TAMANOS = [100, 250, 500, 750, 1000, 1500, 2000]
REPETICIONES = 100
SEMILLA = 2026


def medir(funcion, datos):
    copia = list(datos)  # la copia queda fuera del cronómetro
    gc.disable()
    inicio = time.perf_counter_ns()
    resultado = funcion(copia)
    fin = time.perf_counter_ns()
    gc.enable()
    assert resultado == sorted(datos)
    return (fin - inicio) / 1e6


def main():
    rng = random.Random(SEMILLA)
    filas = []
    for n in TAMANOS:
        for rep in range(1, REPETICIONES + 1):
            # la misma lista aleatoria para los tres algoritmos, en orden alternado
            datos = [rng.randint(0, 1_000_000) for _ in range(n)]
            orden = list(ALGORITMOS)
            rng.shuffle(orden)
            for nombre in orden:
                filas.append({"algoritmo": nombre, "n": n, "repeticion": rep,
                              "tiempo_ms": round(medir(ALGORITMOS[nombre], datos), 5)})
        print(f"n={n} listo")

    filas.sort(key=lambda f: (list(ALGORITMOS).index(f["algoritmo"]), f["n"], f["repeticion"]))
    salida = {
        "meta": {
            "descripcion": "Tiempo de ejecución de algoritmos de ordenamiento sobre listas de enteros aleatorios",
            "fecha": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "lenguaje": f"Python {platform.python_version()}",
            "sistema": f"{platform.system()} {platform.release()}",
            "procesador": platform.machine(),
            "algoritmos": list(ALGORITMOS),
            "tamanos": TAMANOS,
            "repeticiones": REPETICIONES,
            "semilla": SEMILLA,
            "rango_valores": [0, 1_000_000],
            "unidad": "ms",
            "cronometro": "time.perf_counter_ns, recolector de basura desactivado durante la medición",
        },
        "mediciones": filas,
    }

    with open("datos/mediciones.json", "w", encoding="utf-8") as f:
        json.dump(salida, f, ensure_ascii=False, indent=1)
    with open("datos/mediciones.csv", "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["algoritmo", "n", "repeticion", "tiempo_ms"])
        escritor.writeheader()
        escritor.writerows(filas)
    embeber_en_html()


def embeber_en_html():
    with open("datos/mediciones.json", encoding="utf-8") as f:
        salida = json.load(f)
    marca_ini, marca_fin = '<script type="application/json" id="datos">', "</script>"
    with open("index.html", encoding="utf-8") as f:
        html = f.read()
    ini = html.index(marca_ini) + len(marca_ini)
    fin = html.index(marca_fin, ini)
    html = html[:ini] + json.dumps(salida, ensure_ascii=False, separators=(",", ":")) + html[fin:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    embeber_en_html() if "--solo-html" in sys.argv else main()
