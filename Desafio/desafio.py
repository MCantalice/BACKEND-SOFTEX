def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    
    return num1 / num2

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    operacao = input("Qual operação você quer? (+, -, *, /): ")

    if operacao == '+':
        resultado = somar(numero1, numero2)
    elif operacao == '-':
        resultado = subtrair(numero1, numero2)
    elif operacao == '*':
        resultado = multiplicar(numero1, numero2)
    elif operacao == '/':
        
        resultado = dividir(numero1, numero2)
    else:
       
        print("Erro: operação inválida")
        
        exit()

except ValueError:
    
    print("Erro: valor inválido")
except ZeroDivisionError:
    
    print("Erro: divisão por zero")
except:
    
    print("Ocorreu um erro inesperado.")

else:
    print(f"O resultado da sua conta é: {resultado}")
    

finally:
    print("Fim do programa")