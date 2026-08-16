# Exercício 3 — Cálculo da Área do Círculo
import math 
# pede o valor do raio e converte para número decimal (float)
r = float(input('Raio do círculo: '))
# calcula a área usando a fórmula: pi * r², se não quiser usar a biblioteca da para colocar o valor de pi aqui ao invés de math.pi
area = math.pi * r ** 2
print('Área:', area)