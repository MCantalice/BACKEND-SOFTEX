alunos = [{"nome": "Ana", "nota": 7.5, "frequencia": 80},
    {"nome": "Bruno", "nota": 6.0, "frequencia": 70},
    {"nome": "Carla", "nota": 4.5, "frequencia": 90}]

for aluno in alunos:
    nome = aluno["nome"]
    nota = aluno["nota"]
    frequencia = aluno["frequencia"]

    if nota >= 7.0 and frequencia >= 75:
         status = "Aprovado"
    elif nota >= 5.0 and frequencia <= 75:
        status = "Recuperação"
    else:
        status = "Reprovado"

    print(f"{nome}: {status}")