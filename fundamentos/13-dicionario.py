filmInception = {
    'title': 'Inception',
    'yearRelease': 2010,
    'imbdRating': 8.8,
    'genre': ['Sci-fi', 'Action', 'Thriller']
}

print(filmInception)
print(len(filmInception))
print(type(filmInception))

# 1 - Recupera um elemento do dicionario
print(filmInception['genre'])
print(filmInception.get('imdbRating'))

# 2 - Busca apenas as chaves do dicionário
print(filmInception.keys())

# 3 - Busca apenas os valores do dicionário
print(filmInception.values())

# 4 - Busca itens do dicionário com chave e valor
print(filmInception.items())

# 5 - Adiciona itens no dicionario
filmInception['director'] = 'Christopher Nolan'
print(filmInception)

# 6 - Atualiza itens no dicionário
filmInception.update({'imdbRating': 8.7})
print(filmInception)

# 7 - Remove item
filmInception.pop('director')
print(filmInception)