# 💱 Conversor de Moedas com API REST

Projeto desenvolvido em **Python** para praticar consumo de **API REST**, requisições HTTP, JSON, dicionários, tratamento de erros e organização de código.

A aplicação consulta cotações através da **AwesomeAPI** e realiza conversões de moedas através de uma interface web desenvolvida com Flask.

## 🛠️ Tecnologias

* Python
* Flask
* Requests
* HTML
* CSS
* JavaScript
* Jinja2
* API REST
* JSON
* Git e GitHub

## 📌 Funcionalidades

* Consulta de cotações através de API REST
* Conversão entre Real, Dólar, Euro e Iene
* Conversão entre diferentes pares de moedas
* Interface web com Flask
* Validação dos valores informados
* Tratamento de erros
* Utilização de dicionários
* Organização do projeto em módulos
* Histórico de conversões
* Exibição dinâmica dos dados utilizando Jinja2
* Abertura e fechamento do histórico utilizando JavaScript
* Animação do painel de histórico utilizando CSS
* Fechamento do histórico através de botão ou ao clicar fora do painel

## 📂 Estrutura

```text
Conversor-de-Moedas-com-API-REST/

│
├── app.py
├── main.py
├── conversor.py
├── api.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── .gitignore
└── README.md
```

## 🌐 API

O projeto utiliza a **AwesomeAPI** para obter as cotações.

A aplicação realiza uma requisição HTTP para a API e recebe os dados em formato JSON.

A resposta JSON é convertida para um dicionário Python, permitindo que o programa acesse os valores das cotações e realize os cálculos necessários.

Também foram implementados tratamentos para erros de requisição e dados inexistentes na resposta da API.

## 📜 Histórico de conversões

O projeto possui um histórico das conversões realizadas durante a execução da aplicação.

Cada conversão armazena:

* Valor informado
* Moeda de origem
* Moeda de destino
* Resultado da conversão
* Cotação utilizada
* Símbolo da moeda de origem
* Símbolo da moeda de destino

Os dados são armazenados em uma lista de dicionários e enviados pelo Flask para a interface utilizando **Jinja2**.

O histórico possui uma interface interativa desenvolvida com **JavaScript**, permitindo:

* Abrir o histórico através de um botão
* Fechar através do botão `×`
* Fechar ao clicar fora do painel
* Exibir o painel com uma animação utilizando CSS

> O histórico é armazenado apenas durante a execução da aplicação. Ao reiniciar o servidor Flask, os registros são perdidos.

## ▶️ Como executar

```bash
git clone https://github.com/juliocesar-ADS/Conversor-de-Moedas-com-API-REST.git

cd Conversor-de-Moedas-com-API-REST

pip install -r requirements.txt

python app.py
```

Depois, acesse o endereço exibido pelo Flask no terminal.

## 📚 O que estou praticando

* Python
* Funções e módulos
* Dicionários
* Listas
* Tratamento de exceções
* Requisições HTTP
* API REST
* JSON
* Flask
* Jinja2
* HTML
* CSS
* JavaScript
* Manipulação de classes CSS
* Eventos JavaScript
* Git e GitHub
