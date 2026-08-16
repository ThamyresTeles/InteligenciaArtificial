# Exercício 27 — Anagramas
def eh_anagrama(a, b):
    return sorted(a.replace(' ', '').lower()) == sorted(b.replace(' ', '').lower()) # remove espaços, coloca em minúsculo e compara letras ordenadas
a = input('Primeira palavra: ') # duas palavras fornecidas pelo usuário
b = input('Segunda palavra: ')
print('Anagramas' if eh_anagrama(a, b) else 'Não são anagramas')