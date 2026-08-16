# Exercício 35 — Números Fibonacci Até N
n = int(input('Número n (limite): '))             # Lógica parecida com a ex 8
a, b = 0, 1                                           # mas aqui paramos quando o valor ultrapassa n, enquanto na 8 pode ser por quantidade de termos.
while a <= n: # gera a sequência até n
    print(a)
    a, b = b, a + b