
import random
import time
import ord

def genera(n, min, max):
    temp = []
    for _ in range(n):
        temp.append(random.randint(min, max))
    return temp

def ejecutar_pruebas():

    N = [30, 50, 70, 90, 110]
    
    t_selection = []
    t_bubble = []
    t_insertion = []
    t_gnome = []
    t_exchange = []
    t_merge = []
    t_quick =[]

    for n in N:
 
        lista_original = genera(n, 1, 100)

        l1 = lista_original.copy()
        l2 = lista_original.copy()
        l3 = lista_original.copy()
        l4 = lista_original.copy()
        l5 = lista_original.copy()
        l6 = lista_original.copy()
        l7 = lista_original.copy()

        print(f"\n--- Ordenando listas de tamaño {n} ---")

        # Selection Sort
        t_ini = time.time()
        print(ord.selection_sort(l1))
        t_fin = time.time()
        t_selection.append(t_fin - t_ini)

        # Bubble Sort
        t_ini = time.time()
        print(ord.bubble_sort_brute_force(l2))
        t_fin = time.time()
        t_bubble.append(t_fin - t_ini)

        # Insertion Sort
        t_ini = time.time()
        print(ord.insertion_sort(l3))
        t_fin = time.time()
        t_insertion.append(t_fin - t_ini)

        # Gnome Sort
        t_ini = time.time()
        print(ord.gnome_sort(l4))
        t_fin = time.time()
        t_gnome.append(t_fin - t_ini)

        # Exchange Sort
        t_ini = time.time()
        print(ord.exchange_sort(l5))
        t_fin = time.time()
        t_exchange.append(t_fin - t_ini)

        # Merge Sort
        t_ini = time.time()
        print(ord.merge_sort(l6))
        t_fin = time.time()
        t_merge.append(t_fin - t_ini)

        # Quick Sort
        t_ini = time.time()
        print(ord.quick_sort(l7))
        t_fin = time.time()
        t_quick.append(t_fin - t_ini)


    return N, t_selection, t_bubble, t_insertion, t_gnome, t_exchange, t_merge, t_quick