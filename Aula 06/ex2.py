NOTA_MINIMA= 7.0
NOTA_RECUPERACAO = 5.0

nota= float(input("Que nota você tirou? "))

if nota >= NOTA_MINIMA:
    print("Aprovado!")
elif nota >= NOTA_RECUPERACAO:
    print("Você não foi muito bem, mas ainda consegue recuperar")
else:
    print("Reprovado")