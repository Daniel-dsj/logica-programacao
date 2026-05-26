while True:
    tabuada = int(input("Digite o número que queira saber a tabuada: "))
    print(f"Tabuada do número {tabuada}:")
    
    for i in range(1, 11):
        resultado = tabuada * i
        print(f"{tabuada} x {i} = {resultado}")
        
    print("Deseja ver a tabuada de outro número?\nDigite 1 para SIM ou 2 para NÃO")
    
    escolha = int(input())
    
    if escolha != 1:
        print("Fim do programa!")
        break
