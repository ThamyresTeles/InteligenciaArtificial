# Exercício 38 — Contar Palavras em Texto
text = input('Digite um texto: ')
num_palavras = len(text.split())        #separa palavras com split() e conta
print('Número de palavras:', num_palavras)