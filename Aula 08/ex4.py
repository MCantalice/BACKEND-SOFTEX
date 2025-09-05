def perfil (*dados):
    entrada=""
    for dado in dados:
        entrada+=dado
    return entrada

print(perfil("Meu"," " ,"nome"," ","é"," ","Maria"))