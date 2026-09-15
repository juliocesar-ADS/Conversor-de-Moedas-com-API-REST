# 💱 Conversor de Moedas com API REST

Aplicação web desenvolvida em **Python e Flask** para realizar conversões entre diferentes moedas utilizando dados obtidos através de uma **API REST pública**.

O projeto foi desenvolvido com foco no aprendizado de **Python, consumo de APIs, Flask, requisições HTTP, JSON, HTML, CSS, JavaScript e Git/GitHub**.

## 🌐 Aplicação

🔗 **Aplicação online:** *em breve*

## 🛠️ Tecnologias

* Python
* Flask
* Requests
* HTML5
* CSS3
* JavaScript
* API REST
* JSON
* Jinja2
* Git
* GitHub

## 📌 Funcionalidades

* Conversão entre Real, Dólar, Euro e Iene
* Consulta de cotações através de API REST
* Interface web utilizando Flask
* Validação dos valores informados
* Tratamento de erros
* Histórico de conversões
* Limpeza do histórico
* Interface interativa com JavaScript
* Animações utilizando CSS
* Exibição dinâmica dos resultados utilizando Jinja2


## 🌐 API


O projeto utiliza a Frankfurter API para obter as cotações das moedas.

A aplicação realiza uma requisição HTTP para a API utilizando a biblioteca Requests. A resposta é recebida no formato JSON e convertida para um dicionário Python.

A cotação é obtida através do campo rate retornado pela API.

Exemplo de consulta:

BRL → USD

A aplicação monta dinamicamente o endpoint de acordo com as moedas escolhidas pelo usuário.

O projeto possui tratamento para erros de requisição, dados inválidos e ausência de informações esperadas na resposta da API.

antigamente usava o AwesomeAPI, mas essa api tem limite de requisição.

## 📂 Estrutura do projeto

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

## ▶️ Como executar localmente

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

Execute a aplicação:

```bash
python app.py
```

Depois, acesse o endereço exibido pelo Flask no terminal.

## 📚 O que foi praticado

Durante o desenvolvimento do projeto foram praticados:

* Funções e módulos em Python
* Dicionários e listas
* Tratamento de exceções
* Requisições HTTP
* Consumo de API REST
* JSON
* Flask
* Rotas
* Métodos GET e POST
* `request.form`
* Templates com Jinja2
* HTML
* CSS
* JavaScript
* Manipulação do DOM
* Git e GitHub
* Integração com APIs externas
* Consumo de dados JSON
* Tratamento de respostas HTTP

## 📈 Evolução do projeto

O projeto começou como uma aplicação simples executada pelo terminal e evoluiu para uma aplicação web utilizando Flask.

Durante o desenvolvimento foram adicionados:

* Consumo de API REST
* Tratamento de erros
* Validação de dados
* Interface web
* Histórico de conversões
* Limpeza do histórico
* Interação com JavaScript
* Animações com CSS


> Projeto desenvolvido para fins de estudo e portfólio.

```
```
