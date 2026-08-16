# Exercício 15 — Média de uma Lista
nums = list(map(int, input('Digite números separados por espaço: ').split()))
print('Média:', sum(nums)/len(nums) if nums else 0) # soma os números e divide pela quantidade
# Obs: se a lista estiver vazia, retorna 0 para evitar erro