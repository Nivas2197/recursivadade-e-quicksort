# -------------------------
# Utility Functions
# -------------------------

def indice_menor(lista):
    """Return the index of the smallest element in the list."""
    indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice


def verifica_numero(msg):
    """Recursively request a numeric input from the user."""
    num = input(msg)
    while not num.isnumeric():
        print("⚠️ Invalid input. Please enter a number.")
        num = verifica_numero(msg)
    return int(num)


def forca_opcao(msg, lista_opcoes):
    """Force the user to select an option from a list of choices."""
    opcoes = '\n'.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n-> ")
    while escolha not in lista_opcoes:
        print("⚠️ Invalid choice.")
        escolha = forca_opcao(msg, lista_opcoes)
    return escolha


# -------------------------
# Sorting Algorithms
# -------------------------

def selection_sort(lista):
    """Selection sort (creates a new sorted list)."""
    ordenada = []
    while lista:
        local_menor = indice_menor(lista)
        ordenada.append(lista.pop(local_menor))
    return ordenada


def selection_sort_inplace(lista):
    """In-place selection sort."""
    for i in range(len(lista)):
        local_menor = indice_menor(lista[i:]) + i
        lista[i], lista[local_menor] = lista[local_menor], lista[i]


def bubble_sort(lista):
    """Standard bubble sort (in-place)."""
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def bubble_sort_optimized(lista):
    """Optimized bubble sort with early stopping."""
    j = 0
    while True:
        trocas = 0
        for i in range(len(lista) - 1 - j):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocas += 1
        j += 1
        if trocas == 0:
            break


def quicksort(lista):
    """Recursive quicksort algorithm."""
    if len(lista) < 2:
        return lista
    pivo = lista[0]
    menores = [x for x in lista if x < pivo]
    maiores = [x for x in lista if x > pivo]
    iguais = [x for x in lista if x == pivo]  # handle duplicates
    return quicksort(menores) + iguais + quicksort(maiores)


# -------------------------
# Binary Search / Root Finding
# -------------------------

def raiz_binaria(num, precision=0.001):
    """Find the square root of a number using iterative binary search."""
    ini, fim = 0, num
    while fim - ini > precision:
        chute = (ini + fim) / 2
        if chute**2 > num:
            fim = chute
        else:
            ini = chute
    return chute


def raiz_binaria_recursiva(num, ini=0, fim=None, precision=0.001):
    """Recursive binary search to find square root of a number."""
    if fim is None:
        fim = num
    chute = (ini + fim) / 2
    if fim - ini <= precision:
        return chute
    if chute**2 > num:
        return raiz_binaria_recursiva(num, ini, chute, precision)
    else:
        return raiz_binaria_recursiva(num, chute, fim, precision)


# -------------------------
# Example Usage
# -------------------------

if __name__ == "__main__":
    lista = [3, 4, 1, 5, 2, 7, 6]
    
    print("Original list:", lista)
    
    # Selection sort
    sorted_list = selection_sort(lista[:])
    print("Selection sort (new list):", sorted_list)
    
    # In-place selection sort
    selection_sort_inplace(lista)
    print("Selection sort (in-place):", lista)
    
    # Bubble sort
    lista2 = [3, 4, 1, 5, 2, 7, 6]
    bubble_sort(lista2)
    print("Bubble sort:", lista2)
    
    # Optimized bubble sort
    lista3 = [3, 4, 1, 5, 2, 7, 6]
    bubble_sort_optimized(lista3)
    print("Optimized bubble sort:", lista3)
    
    # Quicksort
    lista4 = [5, 3, 8, 1, 7, 6, 2, 10, 4, 9]
    print("Quicksort:", quicksort(lista4))
    
    # Square roots
    print("Square root of 25 (iterative):", raiz_binaria(25))
    print("Square root of 25 (recursive):", raiz_binaria_recursiva(25))
