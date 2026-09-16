from datetime import date


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.historico = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        return self.livros

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def atualizar_livro(self, titulo, novo_titulo, novo_autor, novo_ano):
        livro = self.buscar_livro(titulo)
        if livro is None:
            return False

        livro.titulo = novo_titulo
        livro.autor = novo_autor
        livro.ano = novo_ano
        return True

    def remover_livro(self, titulo):
        livro = self.buscar_livro(titulo)
        if livro is None:
            return False

        self.livros.remove(livro)
        return True

    def emprestar_livro(self, titulo, pessoa):
        livro = self.buscar_livro(titulo)
        if livro is None or livro.status == "Emprestado":
            return False

        hoje = date.today()
        livro.status = "Emprestado"
        livro.data_emprestimo = hoje
        livro.data_devolucao = None
        livro.pessoa_emprestimo = pessoa
        self.historico.append(
            {"tipo": "emprestimo", "data": hoje, "pessoa": pessoa}
        )
        return True

    def devolver_livro(self, titulo):
        livro = self.buscar_livro(titulo)
        if livro is None or livro.status == "Disponível":
            return False

        hoje = date.today()
        livro.status = "Disponível"
        livro.data_devolucao = hoje
        livro.pessoa_emprestimo = None
        self.historico.append({"tipo": "devolucao", "data": hoje})
        return True

    def obter_relatorio_mes(self, ano, mes):
        emprestados = 0
        devolvidos = 0

        for movimentacao in self.historico:
            data = movimentacao["data"]
            if data.year == ano and data.month == mes:
                if movimentacao["tipo"] == "emprestimo":
                    emprestados += 1
                elif movimentacao["tipo"] == "devolucao":
                    devolvidos += 1

        disponiveis = 0
        emprestados_agora = 0
        for livro in self.livros:
            if livro.status == "Disponível":
                disponiveis += 1
            else:
                emprestados_agora += 1

        return {
            "emprestimos_no_mes": emprestados,
            "devolucoes_no_mes": devolvidos,
            "disponiveis_agora": disponiveis,
            "emprestados_agora": emprestados_agora,
            "total_livros": len(self.livros),
        }