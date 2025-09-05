def buscar_livro (titulo, **kwargs):
    print(f"O título do livro é: {titulo}")
    
   
    for chave, valor in kwargs.items():
        print(f"- {chave}: {valor}")


buscar_livro(titulo="Sobre a brevidade da vida", autor="Sêneca", ano="49 d.C")
