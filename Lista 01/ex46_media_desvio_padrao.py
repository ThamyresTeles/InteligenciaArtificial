# Exercício 46 — Calcular Média e Desvio Padrão
import math             # Lógica parecida com a questão 13 (Média de números),
nums = list(map(float, input('Digite números: ').split()))    # mas aqui acrescentamos o cálculo da variância e raiz quadrada.
mean = sum(nums)/len(nums)                                #calcula média e desvio padrão
var = sum((x-mean)**2 for x in nums)/len(nums)
std = math.sqrt(var)
print('Média:', mean)
print('Desvio padrão:', std)