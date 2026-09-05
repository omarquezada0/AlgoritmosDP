import tkinter as tk
import matplotlib.pyplot as plt
import time
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Suponemos que el primer elemento no ordenado es el menor
        min_idx = i
        # Buscamos en el resto de la lista
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el menor encontrado con el primer elemento actual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort_brute_force(arr):
    n = len(arr)
    # Ciclo externo corre n veces de forma fija
    for i in range(n):
        # Ciclo interno compara elementos adyacentes
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                # Intercambio de elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def generar_graficas():

    tamanos_lista = [30, 50, 70, 90, 110, 130]
    tiempos_selection = []
    tiempos_bubble = []
    
    lbl_estado.config(text="Calculando tiempos...")
    root.update() 
    
    for n in tamanos_lista:
        lista_original = [random.randint(1, 1000) for _ in range(n)]
        
        lista_sel = lista_original.copy()
        lista_bub = lista_original.copy()
        
        tin_ssort = time.time()
        selection_sort(lista_sel)
        tfin_ssort = time.time()
        ttotal_ssort = tfin_ssort - tin_ssort
        tiempos_selection.append(ttotal_ssort)

        tin_bsort = time.time()
        bubble_sort_brute_force(lista_bub)
        tfin_bsort = time.time()
        ttotal_bsort = tfin_bsort - tin_bsort
        tiempos_bubble.append(ttotal_bsort)

    lbl_estado.config(text="¡Gráficas generadas con éxito!")

    plt.figure(figsize=(8, 5))
    
    plt.plot(tamanos_lista, tiempos_selection, marker="o", label="Selection Sort", color="blue")
    plt.plot(tamanos_lista, tiempos_bubble, marker="o", label="Bubble Sort", color="red")
    
    plt.title("Comparación de algoritmos: Selection vs Bubble")
    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.grid()
    
    plt.show()

root = tk.Tk()
root.title("Comparador de Algoritmos")
root.geometry("360x220")

lbl_titulo = tk.Label(root, text="Qué onda Omar, presiona el botón\npara comparar los algoritmos.", font=("Arial", 11))
lbl_titulo.pack(pady=15)

btn_graficar = tk.Button(root, text="Generar Gráficas", command=generar_graficas, width=20, bg="lightgray")
btn_graficar.pack(pady=10)

lbl_estado = tk.Label(root, text="Esperando instrucción...", fg="gray")
lbl_estado.pack(pady=10)

root.mainloop()