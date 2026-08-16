# Exercício 5 — Tabuada
n = int(input('Número para tabuada: '))
# laço que percorre os números de 1 até 10
for i in range(1, 11):
    # mostra a multiplicação no formato: n x i (o i é uma váriavel criada para percorrer o laço) = resultado
    print(f'{n} x {i} = {n * i}')