from datetime import date

from biblioteca import Biblioteca
from livro import Livro
from login import SistemaLogin


def ler_ano():
    while True:
        try:
            ano = int(input("Ano de publicação: "))
            if ano > 0:
                return ano
            print("Digite um ano maior que zero.")
        except ValueError:
            print("Digite um ano válido usando apenas números.")


def cadastrar_livro(biblioteca):
    print("\n--- Cadastrar livro ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = ler_ano()

    if titulo == "" or autor == "":
        print("Título e autor são obrigatórios.")
    elif biblioteca.buscar_livro(titulo) is not None:
        print("Já existe um livro com esse título.")
    else:
        biblioteca.adicionar_livro(Livro(titulo, autor, ano))
        print("Livro cadastrado com sucesso!")


def exibir_catalogo(biblioteca, titulo="Livros cadastrados"):
    livros = biblioteca.listar_livros()
    print(f"\n--- {titulo} ---")
    print(f"Quantidade de livros: {len(livros)}")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return False

    for indice, livro in enumerate(livros, start=1):
        print(f"{indice}. {livro}")
    return True


def listar_livros(biblioteca):
    exibir_catalogo(biblioteca)


def consultar_livro(biblioteca):
    if not exibir_catalogo(biblioteca, "Consultar livro"):
        return

    titulo = input("Título para buscar: ").strip()
    livro = biblioteca.buscar_livro(titulo)

    if livro is None:
        print("Livro não encontrado.")
    else:
        print(f"Livro encontrado: {livro}")


def editar_livro(biblioteca):
    if not exibir_catalogo(biblioteca, "Atualizar livro"):
        return

    titulo = input("Título atual: ").strip()
    livro = biblioteca.buscar_livro(titulo)

    if livro is None:
        print("Livro não encontrado.")
    else:
        novo_titulo = input("Novo título: ").strip()
        novo_autor = input("Novo autor: ").strip()
        novo_ano = ler_ano()
        atualizado = biblioteca.atualizar_livro(
            titulo, novo_titulo, novo_autor, novo_ano
        )

        if atualizado:
            print("Livro atualizado com sucesso!")
        else:
            print("Não foi possível atualizar o livro.")


def excluir_livro(biblioteca):
    if not exibir_catalogo(biblioteca, "Excluir livro"):
        return

    titulo = input("Título do livro: ").strip()
    removido = biblioteca.remover_livro(titulo)

    if removido:
        print("Livro excluído com sucesso!")
    else:
        print("Livro não encontrado.")


def emprestar_livro(biblioteca):
    if not exibir_catalogo(biblioteca, "Emprestar livro"):
        return

    titulo = input("Título do livro: ").strip()
    livro = biblioteca.buscar_livro(titulo)

    if livro is None:
        print("Livro não encontrado.")
    elif livro.status == "Emprestado":
        print(f"Esse livro já está emprestado para {livro.pessoa_emprestimo}.")
    else:
        pessoa = input("Nome da pessoa que receberá o livro: ").strip()
        if pessoa == "":
            print("O nome da pessoa é obrigatório.")
        elif biblioteca.emprestar_livro(titulo, pessoa):
            print(f"Livro emprestado com sucesso para {pessoa}!")


def devolver_livro(biblioteca):
    if not exibir_catalogo(biblioteca, "Devolver livro"):
        return

    titulo = input("Título do livro: ").strip()
    livro = biblioteca.buscar_livro(titulo)

    if livro is None:
        print("Livro não encontrado.")
    elif biblioteca.devolver_livro(titulo):
        print("Livro devolvido com sucesso!")
    else:
        print("Esse livro já está disponível.")


def exibir_relatorio(biblioteca):
    hoje = date.today()
    relatorio = biblioteca.obter_relatorio_mes(hoje.year, hoje.month)

    print("\n--- Relatório da biblioteca ---")
    print(f"Mês de referência: {hoje.strftime('%m/%Y')}")
    print(f"Total de livros: {relatorio['total_livros']}")
    print(f"Disponíveis agora: {relatorio['disponiveis_agora']}")
    print(f"Emprestados agora: {relatorio['emprestados_agora']}")
    print(f"Empréstimos no mês: {relatorio['emprestimos_no_mes']}")
    print(f"Devoluções no mês: {relatorio['devolucoes_no_mes']}")

    if relatorio["total_livros"] == 0:
        print("Nenhum livro cadastrado para detalhar.")
    else:
        exibir_catalogo(biblioteca, "Status atual dos livros")

    if relatorio["emprestimos_no_mes"] == 0 and relatorio["devolucoes_no_mes"] == 0:
        print("Ainda não há empréstimos ou devoluções registrados neste mês.")


def exibir_menu():
    print("\n===== BIBLIOTECA CRUD =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Consultar livro")
    print("4 - Atualizar livro")
    print("5 - Excluir livro")
    print("6 - Emprestar livro")
    print("7 - Devolver livro")
    print("8 - Ver relatório do mês")
    print("0 - Sair")


def realizar_login(sistema_login):
    print("\n===== LOGIN =====")
    nome = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    if sistema_login.autenticar(nome, senha):
        print("Login realizado com sucesso!")
        return True

    print("Usuário ou senha inválidos.")
    return False


def executar():
    sistema_login = SistemaLogin()

    if not realizar_login(sistema_login):
        print("Acesso negado. Programa encerrado.")
        return

    biblioteca = Biblioteca()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_livro(biblioteca)
        elif opcao == "2":
            listar_livros(biblioteca)
        elif opcao == "3":
            consultar_livro(biblioteca)
        elif opcao == "4":
            editar_livro(biblioteca)
        elif opcao == "5":
            excluir_livro(biblioteca)
        elif opcao == "6":
            emprestar_livro(biblioteca)
        elif opcao == "7":
            devolver_livro(biblioteca)
        elif opcao == "8":
            exibir_relatorio(biblioteca)
        elif opcao == "0":
            print("Programa encerrado. Até logo!")
            break
        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    executar()