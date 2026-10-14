movieName = 'Top Gun'

movieDescription = '''
    Top Gun Maverick é um filme de aviação e aventura
    muito consagrado na industria
'''

print(movieName.upper())
print(movieName.lower())
print(movieName.capitalize()) # Primeira letra maiuscula
print(movieName.title()) # Todas as palavras ficam com a primeira letra maiuscula
print(movieName.center(10, '-')) # Retorna string centralizada com caractere de preenchimento
print(movieName.find('u'))
print(movieName.replace('Top', 'Matrix'))
print(movieDescription.replace(','))