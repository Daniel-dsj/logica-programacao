numero = int(input('Escolha o primeiro número: '))

parouimpar = numero % 2

if parouimpar == 0:
    print(f'\nO número {numero} é par')
else:
    print(f'\nO número {numero} é ímpar')
