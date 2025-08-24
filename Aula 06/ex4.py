num1=int(input("Digite um valor: "))
num2=int(input("Digite outro valor: "))
operador=input("Qual operador aritmético? ")

if operador=='+':
    resultado= num1+num2
    print("O resultado é:", resultado)
elif operador=='-':
    resultado= num1-num2
    print("O resultado é:", resultado)
elif operador=='*':
    resultado= num1*num2
    print("O resultado é:", resultado)
elif operador=='/':
    resultado= num1/num2
    print("O resultado é:", resultado)
elif operador=='//':
    resultado= num1//num2
    print("O resultado é:", resultado)
elif operador=='%':
    resultado= num1%num2
    print("O resultado é:", resultado)
else:
    print("Operador inválido")
