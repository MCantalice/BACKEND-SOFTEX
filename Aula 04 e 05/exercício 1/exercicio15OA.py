senha= "Python123"
senha_valida=(not (senha == "") and len (senha) >8 and senha == "Python123" and senha != "123456" )

print(f"A senha é válida? {senha_valida}")