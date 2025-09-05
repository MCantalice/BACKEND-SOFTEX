def cadastrar_usuario(nome,email,**funcao):
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    
    for dados,cadastro in funcao.items():
        print(f"{dados}:{cadastro}")

cadastrar_usuario(nome="Maria", email="Maria@email.com", idade=30, cidade="Recife")