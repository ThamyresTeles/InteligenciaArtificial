# Exercício 50 — Frequência de Letras
from collections import Counter  # Counter cria um dicionário com cada elemento e sua contagem.
n = input('Digite uma string: ').lower()
cnt = Counter(ch for ch in n if ch.isalpha())     # percorre cada caractere e conta apenas letras
for ch, c in cnt.items():
    print(ch, c)