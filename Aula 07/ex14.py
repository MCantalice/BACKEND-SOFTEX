clientes=["João", "Maria", "José"]
saldos=[1500, 2500, 800]

for cliente, saldo in zip(clientes, saldos): 
    print(f"{cliente} tem saldo: R${saldo}.") 
