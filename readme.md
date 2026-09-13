# 💱 Conversor de Moedas com API REST

Projeto desenvolvido em **Python** para praticar consumo de **API REST**, requisições HTTP, JSON, dicionários, tratamento de erros e organização de código.

<<<<<<< HEAD
O programa consulta cotações através da **AwesomeAPI** e realiza conversões entre moedas.

> 🚧 Projeto em desenvolvimento.
=======
A aplicação consulta cotações através da **AwesomeAPI** e realiza conversões de moedas através de uma interface web desenvolvida com Flask.
>>>>>>> cba9950 (feat: adiciona historico interativo de conversões)

## 🛠️ Tecnologias

* Python
* Flask
* Requests
<<<<<<< HEAD
=======
* HTML
* CSS
* JavaScript
* Jinja2
>>>>>>> cba9950 (feat: adiciona historico interativo de conversões)
* API REST
* JSON
* HTML
* CSS
* Git e GitHub

## 📌 Funcionalidades

* Consulta de cotações através de API REST
* Conversão entre Real, Dólar, Euro e Iene
<<<<<<< HEAD
* Conversão entre diferentes moedas
=======
* Conversão entre diferentes pares de moedas
>>>>>>> cba9950 (feat: adiciona historico interativo de conversões)
* Interface web com Flask
* Utilização de dicionários
<<<<<<< HEAD
* Validação dos valores informados
* Tratamento de erros de entrada e da API
* Timeout nas requisições
* Organização do código em módulos
=======
* Organização do projeto em módulos
* Histórico de conversões
* Exibição dinâmica dos dados utilizando Jinja2
* Abertura e fechamento do histórico utilizando JavaScript
* Animação do painel de histórico utilizando CSS
* Fechamento do histórico através de botão ou ao clicar fora do painel
>>>>>>> cba9950 (feat: adiciona historico interativo de conversões)

## 📂 Estrutura

```text
Conversor-de-Moedas-com-API-REST/

│
├── app.py
├── api.py
├── conversor.py
├── main.py
├── templates/
├── static/
├── requirements.txt
├── .gitignore
└── README.md
```

### Arquivos

**app.py**
Controla a aplicação Flask, formulário, conversões e mensagens de erro.

**api.py**
Responsável pela comunicação com a API e obtenção das cotações.

**conversor.py**
Responsável pelos cálculos e validação dos valores.

**main.py**
Versão inicial do conversor executada pelo terminal.

## 🌐 API utilizada

O projeto utiliza a **AwesomeAPI** para obter as cotações.

<<<<<<< HEAD
Exemplo:

```text
GET /json/last/USD-BRL
```

A resposta é recebida em JSON e os dados são utilizados pelo programa.

As requisições possuem **timeout de 5 segundos** e o projeto trata erros de conexão, respostas HTTP, dados inesperados e valores que não podem ser convertidos.
=======
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
>>>>>>> cba9950 (feat: adiciona historico interativo de conversões)

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/juliocesar-ADS/Conversor-de-Moedas-com-API-REST.git
```

Entre na pasta:

```bash
cd Conversor-de-Moedas-com-API-REST
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python app.py
```

## 📚 O que estou praticando

* Python
* Funções
* Dicionários
<<<<<<< HEAD
* Flask
* HTML e CSS
=======
* Listas
>>>>>>> cba9950 (feat: adiciona historico interativo de conversões)
* Tratamento de exceções
* Requisições HTTP
* API REST
* JSON
<<<<<<< HEAD
* Git e GitHub


=======
* Flask
* Jinja2
* HTML
* CSS
* JavaScript
* Manipulação de classes CSS
* Eventos JavaScript
* Git e GitHub
>>>>>>> cba9950 (feat: adiciona historico interativo de conversões)
