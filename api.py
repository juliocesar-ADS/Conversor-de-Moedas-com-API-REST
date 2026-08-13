import requests


def obter_cotacao(moeda):
        
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"

        resposta = requests.get(url)

        resposta.raise_for_status()

        dados = resposta.json()

        moeda_api = moeda.replace("-", "")

        return float(dados[moeda_api]["bid"])
    
    except requests.exceptions.RequestException:
        print("Erro ao consultar a API.")
        return None
