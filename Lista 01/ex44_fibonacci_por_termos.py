# Exercício 44 — Fibonacci em Nível
terms = int(input('Número de termos: '))    # Lógica parecida com a questão 35 (Fibonacci até N),
a, b = 0, 1                                 # mas aqui o limite é o número de termos, não o valor máximo.
for _ in range(terms):                      # gera a sequência
    print(a)
    a, b = b, a + b