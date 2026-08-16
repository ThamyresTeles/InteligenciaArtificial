# Exercício 34 — Contador de Vogais
n = input('Digite uma palavra: ').lower() # deixa tudo minusculo
vogais = 'aeiou'                          #percorre cada caractere e soma se for vogal
count = sum(1 for ch in n if ch in vogais)
print('Vogais:', count)