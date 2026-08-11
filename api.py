import requests


def obter_cotacao(moeda):

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"

    resposta = requests.get(url)

    dados = resposta.json()

    moeda_api = moeda.replace("-", "")

    return float(dados[moeda_api]["bid"])
