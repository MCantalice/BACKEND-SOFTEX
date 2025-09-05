def vogais (vogal):
    vogais= "aeiouAEIOUÃÓÉ"
    contador=0
    for letras in vogal:
        if letras in vogais:
            contador+=1
            
    return contador
        
print(vogais("A quantidade de vogais no meu texto é:"))