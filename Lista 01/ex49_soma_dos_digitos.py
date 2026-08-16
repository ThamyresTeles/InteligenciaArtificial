# Exercício 49 — Soma dos Dígitos
# Enunciado: Calcule a soma dos dígitos de um número.

# n: valor informado pelo usuário
n = input('Digite um inteiro: ')
print(sum(int(d) for d in n if d.isdigit()))
