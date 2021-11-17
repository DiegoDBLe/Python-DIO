# CRIE UM ALGORITIMO QUE MOSTRE SOMENTE OS NUMEROS PRIMOS DO NUMERO DIGITADO:

a = int(input('Entre com um número: '))
div = 0
for x in range(1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div += 1

if div == 2:
    print('número {} é primo '.format(a))
else:
    print('numero {} não é primo'.format(a))

# EXPLICAÇÃO: SOLICITADO UM NUMERO, FAZ UM FOR COM UMA VARIAVEL LOCAL CHAMADA DE 'X' ONDE O FOR COMEÇA DE 1 ATE O NUMERO DIGITADO +1, CRIA-SE UMA VARIAVEL
# CHAMADA RESTO QUE RECEBE O NUMERO DIGITADO(a), RESTO DA DIVISÃO(%), PELO O NUMERO DA SEQUENCIA DO FOR(x). PRINTA-SE NA TELA OS NUMEROS DA SEUQNECIA DO FOR, E
# O RESULTADO DO RESTO, CRIA-SE UMA CONDICIONAL QUE SE O RESTO DA DIVISÃO FOR IGUAL A 0 A VARIAVEL DIV VAI SER ACRESCIDA DE +1 OU SEJA ESSA VARIAVEL VAI CONTAR
# QUANTOS NUMEROS DO RESTO SÃO IGUAIS A 0, CRIA-SE OUTRTA CONDICIONAL PARA VERIFICAR SE A VARIAVEL DIV FOR IGUAL A 2 OU SEJA SE A DIV TIVER DOIS NUMEROS QUE
# FOR IGUAL A 0 ENTÃO O NUMERO É PRIMO, POIS O NUMERO PRIMO SÓ É DIVISIVEL POR ELE MESMO E POR 1 E SEU RESTO É 0


#CRIAR UM AGORITIMO PARA MOSTRAR TODOS OS NUMEROS PRIMOS ATÉ O NUMERO DIGITADO:

b = int(input('Digite um numero para saber todos os numeros primos ate ele: '))
for num in range(b+1):
    div = 0

    for x in range(1, num+1):
        restoDivisao = num % x

        if restoDivisao == 0:
            div += 1
    if div == 2:
        print(num)







