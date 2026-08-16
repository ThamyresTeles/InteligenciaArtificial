# Exercício 37 — Funções Recursivas
def fatorial(n):                # Lógica igual à questão 9 (Fatorial de um Número),
    if n <= 1:                        # mas aqui usamos recursão, enquanto na 9 usamos loop.
        return 1                      #aqui eu trouxe o exemplo sem usar o import de math
    return n * fatorial(n-1)
n = int(input('n: '))
print('Fatorial:', fatorial(n))