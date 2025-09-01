nomes=["Teclado", "Mouse"]
precos=[250,120]
estoque=[10,25]

for nome,preco,estoque in zip(nomes, precos,estoque):
    print(f"O produto {nome}, tem o custo R$: {preco}. Ainda disponível no estoque: {estoque} unidades.")