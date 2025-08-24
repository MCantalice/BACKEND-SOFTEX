status=(input("Digite o status do pedido: "))

match status:
    case 'recebido':
        print("O pedido foi recebido!")
    case 'em_preparacao':
        print("O pedido está em preparação!")
    case 'entregue':
        print("O pedido foi entregue!")
    case _:
        print("Status inválido")