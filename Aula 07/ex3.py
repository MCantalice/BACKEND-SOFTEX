vendas_semanas= [1200, 1500, 1100, 2000, 2500, 1800, 1300]
dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

total_vendas= sum(vendas_semanas)
print(f"O total de vendas da semana foi: {total_vendas}")

menor_vendas= min(vendas_semanas)
indice_menor = vendas_semanas.index(menor_vendas)
dia_menor= dias_semana[indice_menor]

print("O menor dia de vendas durante a semana foi:", dia_menor)