# Exercício 12 — Contagem de Caracteres
s = input('Digite uma palavra: ')
counts = {}
for letra in s:                                   #  aqui se a letra já existe no dicionário, soma +1
    counts[letra] = counts.get(letra, 0) + 1      # se não existe, começa em 0 e soma +1
for letra, quantidade in counts.items():
    print(f"'{letra}': {quantidade}")             # quando a letra se repete dentro de uma palavra, vai mostrar o nº de vezes