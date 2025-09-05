def atualizar_perfil (perfil, **kwargs):
    perfil.update(kwargs)
    return perfil

perfil= {'nome': 'João', 'idade': 30}
print(perfil)

atualizaçao=atualizar_perfil(perfil, idade=31, cidade="Rio de Janeiro")
print(atualizaçao)
