# Exercício 36 — Gerador de Senhas
import random, string       # usamos random para gerar valores e sorteamos caracteres para formar uma senha.
length = int(input('Tamanho da senha: '))
chars = string.ascii_letters + string.digits  #sorteia caracteres de letras e números
senha = ''.join(random.choice(chars) for _ in range(length))
print('Senha gerada:', senha)