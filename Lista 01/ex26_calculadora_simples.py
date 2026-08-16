# Exercício 26 — Calculadora Simples
# Enunciado: Faça adição, subtração, multiplicação e divisão.

# a: primeiro valor informado
a = float(input('Primeiro número: '))
op = input('Operação (+ - * /): ')
# b: segundo valor informado
b = float(input('Segundo número: '))
# avalia a condição para decidir o próximo passo
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b if b != 0 else 'Erro: divisão por zero')
else:
    print('Operação inválida')
