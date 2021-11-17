# SEM O MÉTODO INIT E PASSANDO OS PARAMETROS NO PRÓPRIO MÉTODO
class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print('A soma é : {}'.format(calculadora.soma(10, 15)))
print('A Subtração é : {}'.format(calculadora.subtracao(20, 50)))
print('A Multiplicação é : {}'.format(calculadora.multiplicacao(10, 6)))
print('A Divisão é : {}'.format(calculadora.divisao(110, 2)))
