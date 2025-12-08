import requests
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Maria1994",
    database="CEP")
cursor=conexao.cursor()

cep = input("Digite apenas o número do CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)

if resposta.status_code != 200:
    print("Erro ao acessar a API. Código:", resposta.status_code)
    exit()

dados = resposta.json() 

print("CEP:", dados.get("cep"), 
      ", logradouro:", dados.get("logradouro"),
      ", bairro:", dados.get("bairro"),
      ", localidade:", dados.get("localidade"),
      ", UF:", dados.get("uf"))

cep_hifen = dados.get("cep", "").replace("-", "")

sql="""INSERT INTO enderecos(cep, logradouro, bairro, localidade, UF) VALUES(%s,%s,%s,%s,%s)"""  

valores = (
    cep_hifen, 
    dados.get("logradouro"),
    dados.get("bairro"),
    dados.get("localidade"),
    dados.get("uf")
)

cursor.execute(sql, valores)
conexao.commit()

print("Dados salvos com sucesso!")

cursor.close()
conexao.close()