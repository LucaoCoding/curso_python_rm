# 1

primeiroNome = input('Digite o nome: ')
segundoNome = input('Digite o sobrenome: ')

nomeFormatado = f'{segundoNome} {primeiroNome}'
print(nomeFormatado)

# 2

texto = 'Python é muito interessante'
palavras = texto.split()
textoInvertido = ' '.join(palavras[::-1])
print(textoInvertido)

# 3

texto1 = 'arara'
texto2 = 'python'

texto1_format = texto1.lower().replace(' ', '')
texto2_format = texto2.lower().replace(' ', '')

palindromo1 = texto1_format == texto1[::-1]
palindromo2 = texto1_format == texto2[::-1]