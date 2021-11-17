# UTILIZAR E INTERAGIR COM MÓDULOS; IMPORTÂNCIA DE UTILIZAR MÓDULOS; APRENDER SOBRE FUNÇÕES ANÔNIMAS

from aula7Dio_televisao import Televisao
from aula7Dio_calculadora1 import Calculadora
from aula8Dio_contador_letras import contador_letras, teste

# FAZENDO A IMPORTAÇÃO DA CLASSE E DOS MÉTODOS
televisao = Televisao()
print('Televisão Ligada? \033[1;31m{}\033[m: '.format(televisao.ligada))
televisao.power()
print('Televisão Ligada? \033[1;32m{}\033[m:'.format(televisao.ligada))

print('*' * 20)

# FAZENDO A IMPORTAÇÃO DA CLASSE E DOS MÉTODOS
calculadora = Calculadora(2, 5)
print('A soma = {}'.format(calculadora.soma()))
print('A multiplicação = {}'.format(calculadora.multiplicacao()))

print('*' * 20)

# FAZENDO A IMPORTAÇÃO SOMENTE DO MÉTODO CONTADOR DE LETRAS. NÃO PRECISA FAZER INSTANCIAMENTO POIS NÃO TEM CLASSE PRA INSTANCIAR
lista = ['cachorro', 'gato', 'elefante']
print('total de letras por palavras {} da lista: {}'.format(lista, contador_letras(lista)))
print(teste())
