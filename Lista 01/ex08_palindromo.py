# Exercício 8 — Verificação de Palíndromo
# Pede uma palavra ao usuário, tira espaços extras (.strip) e coloca tudo em minúsculo (.lower)
n = input('Digite uma palavra: ').strip().lower()
# Verifica se a palavra é igual à sua versão invertida ([::-1]), esse comando, é truque em python para inverter a palavra
if n == n[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')