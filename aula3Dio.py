# CALCULO DE 4 NOTAS E MÉDIA DE NOTAS + VALIDAÇÃO A CADA PERGUNTA + VALIDAÇÃO NO FINAL
a = int(input('Digita a nota do primeiro Bimestre: '))
if a > 10:
    a = int(input('NOTA INVÁLIDA. \nDigite a nota correta do Primeiro Bimestre: '))
b = int(input('Digite a nota do segundo  Bimestre: '))
if b > 10:
    b = int(input('NOTA INVÁLIDA. \nDigite a nota correta do Segundo Bimestre: '))
c = int(input('Digite a nota do terceiro Bimestre: '))
if c > 10:
    c = int(input('NOTA INVÁLIDA. \nDigite a nota correta do Terceiro Bimestre: '))
d = int(input('Digite a nota do quarto Bimestre: '))
if d > 10:
    d = int(input('NOTA INVÁLIDA. \nDigite a nota correta do Quarto Bimestre: '))

media = (a + b + c + d) / 4

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('media: {}'.format(media))
else:
    print('Error: Alguma nota foi informada errada')





# CALCULO DE 4 NOTAS E MÉDIA DE NOTAS + VALIDAÇÃO NO FINAL

# a = int(input('Digita a nota do primeiro Bimestre: '))
# b = int(input('Digite a nota do segundo  Bimestre: '))
# c = int(input('Digite a nota do terceiro Bimestre: '))
# d = int(input('Digite a nota do quarto   Bimestre: '))
# media = (a + b + c + d) / 4
# if a <= 10 and b <= 10 and c <=10 and d<=10:
#     print('media: {}'.format(media))
# else:
#     print('Error: Alguma nota foi informada errada')



# # SABER SE FOI DIGITADO ALGUM NUMERO PAR NOS DOIS CAMPOS SOLICITADOS
# a = int(input('Digite o primeiro numero: '))
# b = int(input('Digite p segundo numero:  '))
#
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado uma numero par')
# else:
#     print('Não foi digitado nenhum numero par')



# MOSTRAR SE O NUMERO É PAR OU IMPAR

# a = int(input('Digite o primeiro numero: '))
# resto = a % 2
# if resto == 0:
#     print('Numero é par')
# else:
#     print('Numero é impar')


#SOMA DE TRES VALORES E MOSTRA QUAL O MAIOR

# a = int(input('Digite o primeiro numero: '))
# b = int(input('Digite o segundo numero:  '))
# c = int(input('Digite o terceiro numero: '))
#
# if a > b and a > c:
#     print('O maior numero é : {}'.format(a))
# elif b > a and b > c:
#     print('O maior numero é: {}'.format(b))
# else:
#     print('O maior numero é: {}'.format(c))
# print('Final do Programa...:')