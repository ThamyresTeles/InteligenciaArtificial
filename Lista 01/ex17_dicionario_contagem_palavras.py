# Exercício 17 — Dicionário de Contagem de Palavras
text = input('Digite um texto: ')
words = text.split()  # aqui o é separado o texto em palavras
freq = {}             # Cria um dicionário para armazenar a frequência
for w in words:       # Percorre cada palavra
    freq[w] = freq.get(w, 0) + 1
for w, c in freq.items():  # Mostra a frequência de cada palavra
    print(f'{w}: {c}')