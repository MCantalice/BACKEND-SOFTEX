km_rodado= float(input("Quantos km percorridos? "))
dias= int(input("Quantos dias ultilizou o carro? "))

km=km_rodado * 0.15
diass= + dias * 60

print(f"O valor a pagar é: R$ {km + diass}")
