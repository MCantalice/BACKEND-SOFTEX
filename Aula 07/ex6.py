arquivos=['documento.pdf', 'foto.jpg', 'relatorio.pdf', 'planilha.xlsx']
pdf_files = [arquivo for arquivo in arquivos if arquivo.endswith('.pdf')]

print(pdf_files)
