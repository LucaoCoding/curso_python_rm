movieName = 'Top Gun'

# string[inicio:fim:passo] = 
# indice começa na posição 0 | indice final -1
# passo - determina o incremento

# 1 - Buscar toda string a partir da primeira posição
print(movieName[0:])

# 2 - Buscar toda string até a ultima posição
print(movieName[:7])

# 3 - Buscar toda string da terceira até a ultima posição
print(movieName[2:])

# 4 - Busca toda a string de 2 em 2 caracteres
print(movieName[::2])

# 5 - Busca toda a string em indices impares
print(movieName[1::2])

# 6 - Inverter uma string de trás para frente
print(movieName[::-1])