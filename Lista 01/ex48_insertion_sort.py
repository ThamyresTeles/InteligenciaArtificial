# Exercício 48 — Ordenação por Inserção
def insertion_sort(a):
    for i in range(1, len(a)):        # percorre a lista a partir do segundo elemento
        key = a[i]      # elemento atual que queremos posicionar
        j = i - 1       # índice do elemento anterior
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]   # desloca o elemento para a direita
            j -= 1          # anda uma posição para trás
        a[j+1] = key        # coloca o elemento na posição correta
    return a
arr = list(map(int, input('Lista: ').split()))
print(insertion_sort(arr))