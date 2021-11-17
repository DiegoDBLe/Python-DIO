# FUNÇÃO LAMBDA: É UMA FUNÇÃO ANÔNIMA E SÓ É ÚTIL QUANDO USADO EM UMA LINHA. NO EXEPLO ABAIXO VOU REFAZER O CONTADOR DE LETRAS USANDO LAMBDA

# contador_letras é minha váriavel lambda que recebe a função lambda de uma lista e retorna uma lisa [len(x) conta a quantidade de letras no for]
contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

print('*' * 20)

# USANDO LAMBDA PARA SOMAR DOIS NUMEROS

# soma é minha variavel lambda que recebe a função lambda + dois parametros que retorna a soma desses dois parametros
soma = lambda a, b: a + b
print(soma(5, 2))

print('*' * 20)

# Usando lambda em um dicionário

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: - a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}
print(type(calculadora))
soma = calculadora['soma']
mutiplicacao = calculadora['multiplicacao']
print('A soma = {}'.format(soma(10, 5)))
print('A multiplicação = {}'.format(mutiplicacao(10, 2)))
