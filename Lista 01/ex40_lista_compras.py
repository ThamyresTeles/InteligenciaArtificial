# Exercício 40 — Lista de Compras
# Observação: aqui usamos um loop com comandos. 
items = []
while True:
    cmd = input('(a)diconar, (r)emover, (l)istar, (s)air: ')
    if cmd == 'a':              # avalia o comando
        items.append(input('Item: '))
    elif cmd == 'r':
        it = input('Item a remover: ')
        if it in items:
            items.remove(it)
    elif cmd == 'l':
        print(items)
    else:
        break
print('Lista final:', items)
