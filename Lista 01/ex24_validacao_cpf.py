# Exercício 24 — Validação de CPF
def valida_cpf(cpf: str) -> bool:   
    cpf = ''.join(filter(str.isdigit, cpf)) 
    if len(cpf) != 11 or cpf == cpf[0]*11: # verifica tamanho e se não são todos iguais
        return False
    def digito(digs):    # Função auxiliar para calcular dígitos verificadores
        s = sum(int(d)*w for d, w in zip(digs, range(len(digs)+1, 1, -1)))
        r = (s * 10) % 11
        return '0' if r == 10 else str(r)
    d1 = digito(cpf[:9])      # Calcula os dois dígitos verificadores
    d2 = digito(cpf[:9] + d1)
    return cpf.endswith(d1 + d2)
print('Válido' if valida_cpf(input('CPF: ')) else 'Inválido')