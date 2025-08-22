saldo_bancario= 1000

deposito= float(input("Me informe o valor do depósito: "))
saque= float(input("Me informe o valor do saque: "))
juros= float(input("Me informe o valor do juros: "))

saldo_bancario += deposito
saldo_bancario -=saque
saldo_bancario *= juros

print(f"O saldo atualizado é: {saldo_bancario}")



