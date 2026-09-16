class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = "Disponível"
        self.data_emprestimo = None
        self.data_devolucao = None
        self.pessoa_emprestimo = None

    def __str__(self):
        descricao = f"{self.titulo} - {self.autor} ({self.ano})"
        if self.status == "Emprestado":
            return f"{descricao} | Status: {self.status} para {self.pessoa_emprestimo}"
        return f"{descricao} | Status: {self.status}"