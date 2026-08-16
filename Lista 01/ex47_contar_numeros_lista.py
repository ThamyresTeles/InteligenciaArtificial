# Exercício 47 — Contar Números em Lista
nums = list(map(int, input('Digite números: ').split()))
for n in set(nums):                     #percorre cada número único e conta quantas vezes aparece
    print(n, nums.count(n))