lista = [10, 2, 8, 4, 9, 6, 7, 3, 5, 1]
lista_animal = ['Cachorro', 'Gato', 'Elefante', 'Cavalo', 'Vaca']
print('Mostrando o animal na posição 3: {}'.format(lista_animal[3])) #Escolhendo a posição que quero printar
print('Somando todos os numeros da lista: {}'.format(sum(lista))) #somando todos os numeros da lista
print('Mostrando o valor maximo na lista: {}'.format(max(lista))) #mostrando o maior numero da lista
print('Mostrando o valor minimo na lista: {}'.format(min(lista))) #mostrando o menor numero da lista
print('')
print('Mostrando o animal com maior valor: {}'.format(max(lista_animal)))
print('Mostrando o animal com menor valor: {}'.format(min(lista_animal)))
for x in lista_animal:
    print('- {}'.format(x))

# condicional para verificar se existe ou não um animal na lista
if 'Coelho' in lista_animal:
    print('Existe o animal na lista')
else:
    print('Não existe o animal na lista')
    lista_animal.append('Coelho') #adicionando um animal na lista 
    print(lista_animal)

lista_animal.pop() #retirando um animal da lista. OBS: esse método pop remove sempre o ultimo da lista para remover por posição é so colocar o numero da posição entre ()
print(lista_animal)

lista_animal.remove('Elefante') #remove pelo nome
print(lista_animal)

lista.sort()
print('Ordenando a lista : {}'.format(lista)) # método sort() ordena a lista se numero do menor para o maior e se for string em ordem alfabetica
lista_animal.sort()
print('Ordem alfabetica: {}'.format(lista_animal))

lista.reverse()
print('Ordem reversa dos numeros: {}'.format(lista))
lista_animal.reverse()
print('Ordem reversa dos animais: {}'.format(lista_animal))
