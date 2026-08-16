# Exercício 29 — Números FizzBuzz
for i in range(1, 101): # percorre de 1 a 100 e aplica as regras (o 101 é point stop, ou seja, sempre que a função tiver um nº a mais do que é pedido, é porque tem parar naquele º)
    if i % 15 == 0:
        print('FizzBuzz')  # múltiplo de 3 e 5
    elif i % 3 == 0:
        print('Fizz')      # múltiplo de 3
    elif i % 5 == 0:
        print('Buzz')      # múltiplo de 5
    else:
        print(i)           # caso contrário, imprime o número