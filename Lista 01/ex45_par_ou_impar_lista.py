# Exercício 45 — Par ou Ímpar em Lista
nums = list(map(int, input('Digite números: ').split()))
pares = [n for n in nums if n % 2 == 0]       # separa pares e ímpares
impares = [n for n in nums if n % 2 != 0]
print('Pares:', pares)
print('Ímpares:', impares)