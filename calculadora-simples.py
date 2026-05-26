while True:
    n1 = int(input("Digite seu primeiro numero: "))
    n2 = int(input("\nDigite seu segundo numero: "))
    
    print("\nSelecione o numero correspondente a operação que deseje realizar:\n")
    print("1 - Adição\n")
    print("2 - Subtração\n")
    print("3 - Divisão\n")
    print("4 - Multiplicação\n")
    
    escolha = int(input())
    
    if escolha == 1:
        resultado = n1 + n2
        print("\nO resultado da sua adição é: ", resultado)
        
    elif escolha == 2:
        resultado = n1 - n2
        print("\nO resultado da sua subtração é: ", resultado)
        
    elif escolha == 3:
        resultado = n1 / n2
        print("\nO resultado da sua divisão é: ", resultado)
        
    elif escolha == 4:
        resultado = n1 * n2
        print("\nO resultado da sua multiplicação é: ", resultado)
        
    else:
        print("\nEscolha inválida!")
        
    print("\nDeseja reiniciar a calculadora?\nDigite 1 para SIM ou 2 para NÃO\n")
    
    escolha = int(input())
    
    if escolha != 1:
        print("\nCalculadora encerrada!")
        break