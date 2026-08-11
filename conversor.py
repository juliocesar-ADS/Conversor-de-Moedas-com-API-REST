from api import obter_cotacao

def moedacotacao(moeda):

    cotacao = obter_cotacao(moeda)

    valor = float(input("Digite o valor em reais para converter: R$"))

    resultado = valor / cotacao

    print (f"Cotação: R$ {cotacao:.2f}")
    print(f"Valor convertido: {resultado:.2f}")

def moedacotacaoBRL(moeda):

    cotacao = obter_cotacao(moeda)

    valor = float(input("Digite o valor em reais para converter: "))

    resultado = cotacao / valor

    print (f"Cotação:  {cotacao:.2f}")
    print(f"Valor convertido: R${resultado:.2f}")
