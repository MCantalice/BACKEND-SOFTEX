nomes=['João', 'Maria', 'Pedro']
sobrenomes=['Silva', 'Santos', 'Rocha']
nomes_completos= list(map(lambda n,s: f"{n} {s}", nomes, sobrenomes))

print(nomes_completos)