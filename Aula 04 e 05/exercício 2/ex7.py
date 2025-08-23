idade_motorista = int(input("Qual a sua idade? "))
tem_carteira = bool(input("Você tem carteira de motorista? (True/False) "))

pode_dirigir = idade_motorista >= 18 and tem_carteira == True
print(f"Pode dirigir? {pode_dirigir}")