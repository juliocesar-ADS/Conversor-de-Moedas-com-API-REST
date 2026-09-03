# 💱 Conversor de Moedas com API REST

Projeto desenvolvido em **Python** para praticar consumo de **API REST**, requisições HTTP, JSON, dicionários, tratamento de erros e organização de código.

O programa consulta cotações através da **AwesomeAPI** e realiza conversões entre moedas.

> 🚧 Projeto em desenvolvimento.

## 🛠️ Tecnologias

* Python
* Flask
* Requests
* API REST
* JSON
* HTML
* CSS
* Git e GitHub

## 📌 Funcionalidades

* Consulta de cotações através de API REST
* Conversão entre Real, Dólar, Euro e Iene
* Conversão entre diferentes moedas
* Interface web com Flask
* Utilização de dicionários
* Validação dos valores informados
* Tratamento de erros de entrada e da API
* Timeout nas requisições
* Organização do código em módulos

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

Exemplo:

```text
GET /json/last/USD-BRL
```

A resposta é recebida em JSON e os dados são utilizados pelo programa.

As requisições possuem **timeout de 5 segundos** e o projeto trata erros de conexão, respostas HTTP, dados inesperados e valores que não podem ser convertidos.

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
* Flask
* HTML e CSS
* Tratamento de exceções
* Requisições HTTP
* API REST
* JSON
* Git e GitHub


