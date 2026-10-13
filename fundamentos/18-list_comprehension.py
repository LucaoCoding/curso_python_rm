# 1 - Listando valores de 0 a 10 que sejam menores que 4
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# Lista de filmes
movieList = ['Titanic', 'The godfather', 'Inception', 'Jurassic Park']

# 2 - Filmes que possuem a letra 'e' no titulo
movieWithE = [movie for movie in movieList if 'e' in movie.lower()]
print(movieWithE)

# 3 - Filmes que eu assisti
movieWatched = [movie for movie in movieList if movie != 'Jurassic Park']
print(movieWatched)

# 4 - Encontrando um filme pelo nome
while True:
    searchName = input('Digite o nome do filme para buscar na lista (ou sair para encerrar): ')
    if searchName.lower() == 'sair':
        print('Programa encerrado')
        break

    foundMovie = [movie for movie in movieList if searchName.lower() in movie.lower()]
    if foundMovie:
        print(f'Filme encontrado com o nome: {searchName}')
        for foundMovie in foundMovie:
            print(foundMovie)
    else:
        print(f'Nenhum filme foi encontrado com o nome {searchName}. Tente novamente')