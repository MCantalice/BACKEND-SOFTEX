IDADE_MINIMA = 18

idade=int(input("Qual sua idade? "))

if idade >=IDADE_MINIMA:   
    print("O usuário é maior de idade.")
elif idade == 16 or idade == 17:
    print("O usuário tem 16 ou 17 anos.")
else:
    print("O usuário é menor de idade.")
