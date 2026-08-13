# 💱 Conversor de Moedas com API REST

Projeto desenvolvido em **Python** para praticar o consumo de **API REST**, requisições HTTP, JSON, dicionários, tratamento de erros e organização de código.

O programa consulta cotações através da **AwesomeAPI** e realiza conversões de moedas pelo terminal.

> 🚧 Projeto em desenvolvimento.

---

## 🛠️ Tecnologias

- Python
- Requests
- API REST
- JSON
- Git
- GitHub

---

## 📌 Funcionalidades

- Consulta de cotações através de API REST
- Conversão entre Real, Dólar, Euro e Iene
- Menu interativo no terminal
- Utilização de dicionários
- Validação dos valores informados
- Tratamento de erros da API
- Organização do código em módulos

---

## 📂 Estrutura

```text
Conversor-de-Moedas-com-API-REST/
│
├── main.py
├── conversor.py
├── api.py
├── requirements.txt
├── .gitignore
└── README.md
Arquivos

main.py
Controla os menus e a interação com o usuário.

conversor.py
Responsável pelos cálculos e validação dos valores.

api.py
Responsável pela comunicação com a API e obtenção das cotações.

🌐 API utilizada

O projeto utiliza a AwesomeAPI para obter as cotações.

Exemplo:

GET /json/last/USD-BRL

A resposta da API é recebida em JSON e convertida para um dicionário Python.

▶️ Como executar

Clone o repositório:

git clone https://github.com/juliocesar-ADS/Conversor-de-Moedas-com-API-REST.git

Entre na pasta:

cd Conversor-de-Moedas-com-API-REST

Instale as dependências:

pip install -r requirements.txt

Execute:

python main.py
📚 O que estou praticando
Python
Funções
Dicionários
Loops e condicionais
Tratamento de exceções
Requisições HTTP
API REST
JSON
Git e GitHub
🚀 Próximos passos
 Adicionar mais moedas
 Melhorar o tratamento de erros
 Criar histórico de conversões
 Aplicar POO
 Criar testes
 Criar uma API REST própria com Flask