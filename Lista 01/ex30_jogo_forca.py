# Exercício 30 — Jogo da Forca
import random
palavras = ['python', 'banana', 'amigo', 'computador']    # lista de palavras possíveis
pal = random.choice(palavras)                             # sorteia uma palavra e inicializa o estado
state = ['_'] * len(pal)
tentativas = 6
while tentativas > 0 and '_' in state:                    # Loop: continua até acertar ou acabar as tentativas
    print(' '.join(state))
    letra = input('Letra: ')
    if letra in pal:
        for i, ch in enumerate(pal):
            if ch == letra:
                state[i] = letra
    else:
        tentativas -= 1
        print('Erros restantes:', tentativas) 
print('Você ganhou' if '_' not in state else f'Perdeu. Palavra: {pal}')