import requests

#api para puxar os dados da web

def obter_cotacao(moeda):
        
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"

        resposta = requests.get(url, timeout=5)

        resposta.raise_for_status()

        dados = resposta.json()

        moeda_api = moeda.replace("-", "")

        return float(dados[moeda_api]["bid"])
    
    except requests.exceptions.RequestException as erro:
        print(f"Teve um erro em: {erro}")
        return None

    except KeyError as erro:
        print(f"Erro encontrado: {erro}")
        return None

    except ValueError:
        print("Valor recebido não pode ser convertido para número.")
        return None
