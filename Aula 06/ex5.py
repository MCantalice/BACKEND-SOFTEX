numero=int(input("Digite um número de 1 a 7: "))

match numero:
    case 1:
        print("Hoje é domingo!")
    case 2:
        print("Hoje é segunda!")
    case 3:
        print("Hoje é terça!")
    case 4:
        print("Hoje é quarta!")
    case 5:
        print("Hoje é quinta!")
    case 6:
        print("Hoje é sexta!")
    case 7:
        print("Hoje é sábado!")
    case _:
        print("Número inválido")
