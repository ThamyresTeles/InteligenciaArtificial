# Exercício 20 — Matriz Transposta
mat = []          #mat = matriz
rows = int(input('Número de linhas: '))  # rows: variável de qtd de linha
for i in range(rows):
    mat.append(list(map(int, input(f'Linha {i+1}, números separados por espaço: ').split())))
transp = list(map(list, zip(*mat)))  # calcula a transposta da matriz
for row in transp:
    print(row)