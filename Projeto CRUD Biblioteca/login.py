from usuario import Usuario


class SistemaLogin:
    def __init__(self):
        self.usuarios = [
            Usuario("admin", "1234")
        ]

    def autenticar(self, nome, senha):
        for usuario in self.usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                return True
        return False