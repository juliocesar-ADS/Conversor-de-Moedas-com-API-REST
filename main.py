import time
from conversor import moedacotacao, moedacotacaoBRL




#Convertendo moedas estrangeiras em moedas Brasileiras

def conversorbrasileiro():
    while True:
        print("=================================================")
        print("       CONVERSOR DE MOEDAS PARA BRASILEIRA       ")
        print("=================================================")
        print(" 1 - Dólar")
        print(" 2 - Euro")
        print(" 3 - Iene")
        print(" 4 -Voltar\n")

        try:
            opcao = int(input("Digite um numero: "))
        except ValueError:
            print("Digite um valor valido")
            continue
        
        if opcao == 1:
            moedacotacaoBRL("BRL-USD")
            time.sleep(2)

        elif opcao == 2:
            moedacotacaoBRL("BRL-EUR")
            time.sleep(2)

        elif opcao == 3:
            moedacotacaoBRL("BRL-JPY")
            time.sleep(2)

        elif opcao == 4:
            print("Voltando...")
            time.sleep(2)
            break

        else:
            print("opção inválida!")
            time.sleep(2)


# Convertendo moeda Brasileira em moedas Estrangeiras

def conversorestrangeiro():
    while True:
        print("=================================================")
        print("              CONVERSOR DE MOEDAS                ")
        print("=================================================")
        print(" 1 - Dólar")
        print(" 2 - Euro")
        print(" 3 - Iene")
        print(" 4 -Voltar\n")

        try:
            opcao = int(input("Digite um numero: "))
        except ValueError:
            print("Digite um valor valido")
            continue
        

        if opcao == 1:
            moedacotacao("USD-BRL")
            time.sleep(2)

        elif opcao == 2:
            moedacotacao("EUR-BRL")
            time.sleep(2)

        elif opcao == 3:
            moedacotacao("JPY-BRL")
            time.sleep(2)

        elif opcao == 4:
            print("Voltando...")
            time.sleep(2)
            break

        else:
            print("opção inválida!")
            time.sleep(2)

#Menu principal

while True:
    print(" ______________________________________________")
    print("|       CONVERSOR DE MOEDAS COM API REST       |")
    print("|______________________________________________|\n")
    print("(1) - Conversor de moedas Estrangeiras para Brasileira")
    print("(2) - Conversor de moeda Brasileira para Estrangeiras")
    print("(3) - Sair")

    try:
        opcao = int(input("Digite um numero: "))
    except ValueError:
        print("Digite um valor valido")
        continue

    if opcao == 1:
        conversorbrasileiro()
        time.sleep(2)

    elif opcao == 2:
        conversorestrangeiro()
        time.sleep(2)

    elif opcao == 3:
        print("Obrigado por testar a versão teste do nosso conversor de moedas utilizando API REST, ate a proxima...")
        time.sleep(2)
        break