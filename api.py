import requests

#api para puxar os dados da web

def obter_cotacao(moeda):
        
    try:

        de, para = moeda.lower().split("-")

        url = f"https://api.frankfurter.dev/v2/rate/{de}/{para}"

        resposta = requests.get(url, timeout=5)

        resposta.raise_for_status()

        dados = resposta.json()

        return float(dados["rate"])
    
    except requests.exceptions.RequestException as erro:
        print(f"Teve um erro em: {erro}")
        return None

    except KeyError as erro:
        print(f"Erro encontrado: {erro}")
        return None

    except ValueError:
        print("Valor recebido não pode ser convertido para número.")
        return None
