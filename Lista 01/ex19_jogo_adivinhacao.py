# Exercício 19 — Jogo de Adivinhação
import random
secret = random.randint(1, 100)             # sorteia um número entre 1 e 100
print('Adivinhe um número entre 1 e 100')
while True:                                 # Loop: continua pedindo palpites até acertar
    guess = int(input('Seu palpite: '))
    if guess == secret:  # condição de acerto
        print('Acertou!')
        break
    print('Maior' if guess < secret else 'Menor') # dica: informa se o número secreto é maior ou menor