senha="python123"
senha_digitada=""

while senha_digitada != senha:
    senha_digitada=input("Digite uma senha: ")
    if senha_digitada != senha:
        print("Senha incorreta...")

print("Senha correta!")