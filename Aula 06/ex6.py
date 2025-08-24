nota=int(input("Digite uma nota de 1 a 5: "))

match nota:
    case 1:
        print("Obrigada pelo feedback, devemos melhorar.")
    case 2:
        print("Obrigada pelo feedback, podemos melhorar.")
    case 3:
        print("Obrigada pelo feedback, vamos melhorar.")
    case 4:
        print("Obrigada pelo feedback, espero que tenha gostado.")
    case 1:
        print("Obrigada pelo feedback, ficamos felizes.")
    case _:
        print("Nota inválida")