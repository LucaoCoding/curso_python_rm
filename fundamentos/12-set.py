filmSet = {'Inception', 'UP', 'The Dark Knight', 'Pulp Fiction', 'Interstellar'}

print(type(filmSet))

# 1 - Busca tamanho do set
print(len(filmSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {'Leon', True, 1, 8.7}
print(exampleSet)

# 3 - Adiciona item de outro set
filmSet.update(exampleSet)
print(filmSet)

# 4 - Remove um item no set
filmSet.remove(True)
filmSet.remove(8.7)
print(filmSet)