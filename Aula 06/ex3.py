numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 >= numero2 and numero1 >= numero3:
    if numero2 >= numero3:
        print(f"A ordem decrescente é: {numero1}, {numero2}, {numero3}")
    else:
        print(f"A ordem decrescente é: {numero1}, {numero3}, {numero2}")
elif numero2 >= numero1 and numero2 >= numero3:
    if numero1 >= numero3:
        print(f"A ordem decrescente é: {numero2}, {numero1}, {numero3}")
    else:
        print(f"A ordem decrescente é: {numero2}, {numero3}, {numero1}")
else:  
    if numero1 >= numero2:
        print(f"A ordem decrescente é: {numero3}, {numero1}, {numero2}")
    else:
        print(f"A ordem decrescente é: {numero3}, {numero2}, {numero1}")