# - Lista [] é:  Mutavel, consigo alterar uma lista. excluir, alterar, organizar. Lista começa com []
# - Tupla () é: imutavel. Tupla começa com ()
# - Conjunto {} é: Mutavel porém não aceita valor repetido: . Conjunto começa com {}

conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2}
conjunto.add(11) # Adicionando um numero
conjunto.discard(2) # removendo um numero
print('Conjunto de numeros: {}'.format(conjunto))

conjunto_nome = {'Diego', 'Levi', 'Thyci', 'Neurimar'}
print('Conjunto de nomes: {}'.format(conjunto_nome))

# União de conjuntos: Unio o conjunto1 + conjunto2 na variavel conjuntoUniao atraves do metodo union
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9, 10}
conjuntoUniao = conjunto1.union(conjunto2)
print('Unindo os conjuntos 1 {} e o conjunto 2 {} fica Assim: {} '.format(conjunto1, conjunto2, conjuntoUniao))

# Vai mostrar o numero que se repente no conjunto1 e conjunto2
conjuntoInterseccao = conjunto1.intersection(conjunto2)
print('O numero que se repete nos dos conjuntos é : {}'.format(conjuntoInterseccao))

# Vai mostrar a diferença de um conjunto pro outro, o que tem em um conjunto que não trem no outro
conjuntoDifereca = conjunto1.difference(conjunto2)
print('A diferença de um conjunto para o outro é: {}'.format(conjuntoDifereca))

# Vai mostrar a simetria dos dois conjuntos. Ou seja vai mostrar o numeros que nao se repetem
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('A Diferença simetrica é: {}'.format(conjunto_diff_simetrica))

# Vai mostrar se um conjunto é subconjunto do outro. Ou seja se o conjunto que tiver os mesmos numeros que o outro o que tiver menos é subconjunto do outro
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
subConjunto = conjunto_a.issubset(conjunto_b)
print('O Conjunto_a {} é Sub-Conjunto do Conjunto_b ? {} :  {}'.format(conjunto_a, conjunto_b, subConjunto))
print('Conjunto A é SUPER conjunto de B: {}'.format(conjunto_a.issuperset(conjunto_b)))

# Passando uma lista para conjunto: Já que em lista pode colocar nomes repetidos em conjunto não pode
lista = ['cachorro', 'cachorro', 'cachorro', 'gato', 'galinha', 'vaca']
print('Lista de animais: {}'.format(lista))
conjuntoAnimais = set(lista)
print('Lista de animais convertida em conjunto: {}'.format(conjuntoAnimais))

# Voltando de conjunto para lista:

lista_animais = list(conjuntoAnimais)
print('Transformando de conjunto para lista: {}'.format(lista_animais))
