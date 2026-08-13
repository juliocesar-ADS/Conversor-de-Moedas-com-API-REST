from api import obter_cotacao

def obter_valor():
    while True:
        try:
            valor = float(input("Digite o valor em reais para converter: R$"))
            if valor <= 0:
                print("Valor inválido.")
                continue

            return valor
        
        except ValueError:
            print("Somente Números são válidos.")


def moedacotacao(moeda):

    cotacao = obter_cotacao(moeda)
        
    if cotacao is None:
        print("Não foi possivel obter a cotação.")
        return

    valor = obter_valor()
    
    resultado = valor / cotacao

    print (f"Cotação: R$ {cotacao:.2f}")
    print(f"Valor convertido: {resultado:.2f}")


def moedacotacaoBRL(moeda):

    cotacao = obter_cotacao(moeda)
        
    if cotacao is None:
        print("Não foi possivel obter a cotação.")
        return
    
    valor = obter_valor()
    
    resultado = valor * cotacao

    print (f"Cotação:  {cotacao:.2f}")
    print(f"Valor convertido: R${resultado:.2f}")

    
