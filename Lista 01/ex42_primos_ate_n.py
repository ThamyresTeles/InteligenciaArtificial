# Exercício 42 — Números Primos até N
n = int(input('Até n: '))     # obs: aqui usamos um loop e checagem manual
primos = []                   #verifica se cada número é primo
for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primos.append(num)  # adiciona na lista primos definida ali em cima
print(primos)