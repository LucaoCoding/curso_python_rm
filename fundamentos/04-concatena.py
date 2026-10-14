name = input('Digite o nome do filme: ')
yearLaunch = int(input('Digite o ano de lancamento do filme: '))
noteMovie = float(input('Digite a nota do filme: '))

# Alternativa 1
print('Dados do Filme')
print('Nome do filme :', name)
print('Ano de lancamento :', yearLaunch)
print('Nota do filme: ', noteMovie)

# Alternativa 2
print('Nome do filme: ', name, '\nAno de lancamento: ', yearLaunch, '\nNota do filme: ', noteMovie)

# Alternativa 3

print(f'Nome do filme: {name}'
      f'Ano de lancamento: {yearLaunch}'
      f'Nota do filme: {noteMovie}')