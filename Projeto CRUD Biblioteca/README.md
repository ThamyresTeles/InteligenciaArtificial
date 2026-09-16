# Projeto CRUD Biblioteca

Projeto final da aula de Python: um sistema simples de biblioteca executado pelo terminal.

## Funcionalidades

- Cadastrar livros;
- Listar livros cadastrados;
- Consultar um livro pelo título;
- Atualizar os dados de um livro;
- Excluir um livro.
- Login de usuário antes de acessar o sistema.
- Consultar o status de cada livro;
- Registrar empréstimos e devoluções;
- Registrar o nome da pessoa que recebeu cada empréstimo;
- Exibir relatório mensal da biblioteca.

## Conceitos utilizados

- Programação Orientada a Objetos com as classes `Livro`, `Biblioteca`, `Usuario` e `SistemaLogin`;
- Organização do código em módulos com `import`;
- Funções para organizar cada operação do sistema;
- Estruturas condicionais `if`, `elif` e `else`;
- Laços `while` e `for`;
- Lista para armazenar os livros;
- Tratamento de erros com `try` e `except`;
- Métodos e atributos de objetos.
- Uso do módulo `datetime` para registrar as movimentações.

## Como executar

Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

No Windows, também pode ser necessário usar:

```bash
py main.py
```

### Acesso inicial

Para entrar no sistema, use:

```text
Usuário: admin
Senha: 1234
```

Os dados ficam armazenados apenas enquanto o programa está aberto. Ao encerrá-lo, a lista é reiniciada.