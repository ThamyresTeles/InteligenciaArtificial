# Exercício 41 — Remover Duplicatas
nums = list(map(int, input('Digite números separados por espaço: ').split()))
uniq = list(set(nums))  # converte para conjunto (set) e volta para lista
print('Lista sem duplicatas:', uniq)