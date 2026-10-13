# 1 - Função para imprimir uma mensagem
def welcome():
    print('Bem vindo ao sistema de filmes')

for i in range(10):
    welcome()

# 2 - Função para calcular media de notas
def calculate_average():
    num_rating = int(input('Digite quantas avaliações deseja fazer pro filme: '))
    total = 0
    for i in range(num_rating):
        note = float(input('Digite a nota para o filme: '))
        total += note

    if num_rating > 0:
        average = total / num_rating
    else:
        average = 0

    return average

print(f'A média de avaliações é {calculate_average:.2f}')

# 3 - Função para cadastrar um filme:
def create_movie():
    name = input('Digite o nome do filme: ')
    yearLaunch = int(input('Digite o ano de lançamento do filme: '))
    moviePrice = float(input('Digite o preco do filme: '))
    rating = float(input('Digite a nota do filme: '))
    print(f'{name} ({yearLaunch}) tem nota {rating} e custou R${moviePrice}')

create_movie()