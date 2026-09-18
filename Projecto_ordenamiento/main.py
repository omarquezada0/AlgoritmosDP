# Omar Alejandro Quezada Rodríguez

import tkinter as tk
import matplotlib.pyplot as plt
import benchmark

def iniciar_comparacion():

    lbl_estado.config(text="Midiendo tiempos...aguanta we")
    root.update()


    N, t_sel, t_bub, t_ins, t_gno, t_exc, t_mer, t_qui = benchmark.ejecutar_pruebas()

    lbl_estado.config(text="¡Gráfica lista!")


    plt.figure(figsize=(10, 7))

    plt.plot(N, t_sel, marker='o', label="Selection Sort")
    plt.plot(N, t_bub, marker='s', label="Bubble Sort")
    plt.plot(N, t_ins, marker='^', label="Insertion Sort")
    plt.plot(N, t_gno, marker='d', label="Gnome Sort")
    plt.plot(N, t_exc, marker='x', label="Exchange Sort")
    plt.plot(N, t_mer, marker='*', label="Merge Sort")
    plt.plot(N, t_qui, marker='+', label="Quick Sort")

    plt.title("Comparación de 7 Algoritmos de Ordenamiento")
    plt.xlabel("Tamaño de entrada (N)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.show()


root = tk.Tk()
root.title("Comparacion de algoritmos: fuerza bruta vs DyV")
root.geometry("400x200")

lbl_titulo = tk.Label(root, text="Comparador de Algoritmos Fuerza Bruta vs DyV", font=("Arial", 12, "bold"))
lbl_titulo.pack(pady=20)

btn_graficar = tk.Button(root, text="Iniciar Pruebas y Graficar", command=iniciar_comparacion, bg="lightblue", width=25)
btn_graficar.pack(pady=10)

lbl_estado = tk.Label(root, text="Presiona el botón para comenzar.", fg="gray")
lbl_estado.pack(pady=10)

root.mainloop()