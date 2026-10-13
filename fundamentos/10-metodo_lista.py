filmList = ['Inception', 'UP', 'The Dark Knight', 'Pulp Fiction', 'Interstellar']

# 1 - Tamanho da lista
print(len(filmList))

# 2 - Recuperar um item da lista pelo nome
print(filmList.index('UP'))

# 3 - Adicionar item ao final da lista
filmList.append('Lord of the Rings')
print(filmList)

# 4 - Ordenar a lista
filmList.sort()
print(filmList)

# 5 - Copiar os itens de uma lista para outra
filmCopy = filmList.copy()
filmCopy.remove('UP')
print(filmCopy)