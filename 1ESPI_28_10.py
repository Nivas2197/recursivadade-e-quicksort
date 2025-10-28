def indice_menor(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice

def selection_sort(lista):
    ordenada = []
    while lista:
        local_menor = indice_menor(lista)
        menor = lista.pop(local_menor)
        ordenada.append(menor)
    return ordenada

def selection_sort_melhorzinho(lista):
    for i in range(len(lista)):
        local_menor = indice_menor(lista[i:]) + i
        aux = lista[i]
        lista[i] = lista[local_menor]
        lista[local_menor] = aux
    return

'''pontos = [1,2,6,4,3,8,9,10,12,19,5]
selection_sort(pontos)
selection_sort_melhorzinho(pontos)
print(pontos)'''

lista = [3,4,1,5,2,7,6]

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

def bubble_sort_while(lista):
    j = 0
    while True:
        trocas = 0
        for i in range(len(lista)-1-j):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                trocas += 1
        j += 1
        if trocas == 0:
            return

'''print(lista)
bubble_sort_while(lista)
print(lista)'''

def raiz_binaria(num):
    ini = 0
    fim = num
    while fim - ini > 0.001:
        chute = (ini + fim) / 2
        if chute**2 > num:
            fim = chute
        else:
            ini = chute
    return chute

def raiz_binaria_recursiva(num,ini,fim):
    chute = (ini + fim) / 2
    if fim - ini > 0.001:
        if chute**2 > num:
            fim = chute
        else:
            ini = chute
        chute = raiz_binaria_recursiva(num,ini,fim)
    return chute


def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = verifica_numero(msg)                     #versao recursiva
    return int(num)

def forca_opcao(msg,lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while not escolha in lista_opcoes:
        print("Inválido")                                  #versao recursiva
        escolha = forca_opcao(msg,lista_opcoes)
    return escolha


#quicksort
xebec = [5,3,8,1,7,6,2,10,4,9]
def quicksort(lista):
    if len(lista) < 2:
        return lista
    pivo = lista[0]
    menores = [elem for elem in lista if elem < pivo]
    maiores = [elem for elem in lista if elem > pivo]
    menores_ordenados = quicksort(menores)
    maiores_ordenados = quicksort(maiores)
    return menores_ordenados + [pivo] + maiores_ordenados

print(quicksort(xebec))