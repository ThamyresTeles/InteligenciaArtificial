# Exercício 25 — Classificação de Números
nums = list(map(float, input('Digite números separados por espaço: ').split()))
positivos = [n for n in nums if n > 0]  # aqui os numeros é separa os números em três categorias
negativos = [n for n in nums if n < 0]
zeros = [n for n in nums if n == 0]
print('Positivos:', positivos)
print('Negativos:', negativos)
print('Zeros:', zeros)