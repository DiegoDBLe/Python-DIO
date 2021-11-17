# FAZENDO O INSTANCIAMENTO DA CLASS E PASSANDO OS VALORES COMO PARAMETROS QUE DESEJO OBTER O RESULTADO
class Calculadora:

    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b
if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print('A soma é : {}'.format(calculadora.soma()))
    print('A Subtração é : {}'.format(calculadora.subtracao()))
    print('A Multiplicação é : {}'.format(calculadora.multiplicacao()))
    print('A Divisão é : {}'.format(calculadora.divisao()))
