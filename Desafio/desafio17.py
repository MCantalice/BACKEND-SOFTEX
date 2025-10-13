def autenticar(usuario, senha):
    if usuario == "maria" and senha == "1234":
        return True
    else:
        return False

def emprestar_livro(usuario, senha, livro, atrasado):
    if not autenticar(usuario, senha):
        print("Usuário ou senha incorretos.")
        return

    if atrasado:
        print("Você tem livros atrasados! Regularize antes de emprestar novos.")
        return

    print(f"Livro '{livro}' emprestado com sucesso para {usuario}.")

def devolver_livro(livro, dias_atraso):
    multa_por_dia = 2.50
    multa = 0

    if dias_atraso > 0:
        multa = dias_atraso * multa_por_dia
        print(f"O livro '{livro}' está {dias_atraso} dias atrasado.")
        print(f"Multa: R${multa:.2f}")
        processar_pagamento(multa)
    else:
        print(f"Livro '{livro}' devolvido no prazo. Sem multa.")

def processar_pagamento(valor):
    print(f"Processando pagamento de R${valor:.2f}...")
    print("Pagamento realizado com sucesso")

print("=== Sistema de Biblioteca ===")

usuario = input("Usuário: ")
senha = input("Senha: ")

emprestar_livro(usuario, senha, "Harry Potter e a Pedra Filosofal", atrasado=False)

devolver_livro("Harry Potter e a Pedra Filosofal", dias_atraso=3)
