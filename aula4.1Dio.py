# CALCULO DE 4 NOTAS E MÉDIA DE NOTAS + VALIDAÇÃO A CADA PERGUNTA + VALIDAÇÃO NO FINAL
a = float(input('Digita a nota do primeiro Bimestre: '))
while a > 10:
    a = float(input('NOTA INVÁLIDA. \nDigite a nota correta do Primeiro Bimestre: '))
b = int(input('Digite a nota do segundo  Bimestre: '))
while b > 10:
    b = float(input('NOTA INVÁLIDA. \nDigite a nota correta do Segundo Bimestre: '))
c = float(input('Digite a nota do terceiro Bimestre: '))
while c > 10:
    c =float(input('NOTA INVÁLIDA. \nDigite a nota correta do Terceiro Bimestre: '))
d = float(input('Digite a nota do quarto Bimestre: '))
while d > 10:
    d = float(input('NOTA INVÁLIDA. \nDigite a nota correta do Quarto Bimestre: '))

media = (a + b + c + d) / 4

if media >= 7:
    print('Parabéns!! A Média do aluno foi {} o Aluno está APROVADO!'.format(media))
else:
    print('A Média do aluno foi {}. Aluno REPROVADO!! Estude mais'.format(media))
