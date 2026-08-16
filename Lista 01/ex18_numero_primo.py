# Exercício 18 — Número Primo
def eh_primo(n):
    if n < 2:              # números menores que 2 não são primos
        return False
    i = 2                  # verifica divisores até a raiz quadrada de n
    while i*i <= n:
        if n % i == 0:      # se for divisível, não é primo
            return False
        i += 1
    return True             # se não encontrou divisor, é primo
n = int(input('Digite um inteiro: '))
print('Primo' if eh_primo(n) else 'Não primo')