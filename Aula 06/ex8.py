semaforo=(input("Digite a cor do semáforo: "))

match semaforo:
    case 'vermelho':
        print("Não passe!")
    case 'amarelo':
        print("Passe com cuidado!")
    case 'verde':
        print("Passe livre!")
    case _:
        print("Semáforo inválido")