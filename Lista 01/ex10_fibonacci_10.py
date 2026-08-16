# Exercício 10 — Sequência de Fibonacci
def fib(n):
    a, b = 0, 1    # a: primeiro número da sequência, b: segundo número da sequência
    # repete n vezes para gerar os termos
    for _ in range(n):
        print(a)      
        a, b = b, a+b  # atualiza os valores: próximo termo é a soma dos dois anteriores
# gera os 10 primeiros números da sequência
fib(10)