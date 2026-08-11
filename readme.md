# 💱 Conversor de Moedas com API REST

Projeto desenvolvido em **Python** com o objetivo de praticar o consumo de **API REST**, manipulação de **JSON**, requisições HTTP e organização de código em módulos.

O sistema consulta cotações de moedas em tempo real através da **AwesomeAPI** e realiza conversões entre moedas.

> 🚧 **Projeto em desenvolvimento**
>
> Novas funcionalidades serão adicionadas durante o desenvolvimento do projeto.

---

## 📌 Sobre o Projeto

O Conversor de Moedas permite consultar cotações através de uma API REST e realizar conversões utilizando os valores retornados pela API.

O projeto foi desenvolvido como parte dos meus estudos de **Python e desenvolvimento de APIs**, buscando compreender na prática como uma aplicação se comunica com serviços externos.

### Atualmente o projeto possui:

* Consulta de cotação através de API REST
* Conversão de moedas
* Menu interativo no terminal
* Conversão entre Real, Dólar, Euro e Iene
* Separação do projeto em módulos
* Tratamento básico de entradas inválidas
* Requisições HTTP utilizando `Requests`
* Manipulação de dados em formato JSON

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Requests**
* **API REST**
* **JSON**
* **Git**
* **GitHub**

---

## 🌐 API utilizada

O projeto utiliza a **AwesomeAPI** para consultar as cotações das moedas.

A aplicação realiza requisições HTTP para obter os valores atualizados das moedas e utiliza os dados retornados pela API para realizar os cálculos.

---

## 📂 Estrutura do projeto

```text
conversor-moedas/
│
├── main.py
├── conversor.py
├── api.py
├── requirements.txt
├── .gitignore
└── README.md
```

### `main.py`

Responsável pelo menu principal e pela interação com o usuário.

### `conversor.py`

Responsável pela lógica de conversão das moedas.

### `api.py`

Responsável pela comunicação com a API externa e obtenção das cotações.

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta

```bash
cd conversor-moedas
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o projeto

```bash
python main.py
```

---

## 💻 Exemplo de utilização

Ao executar o programa, será apresentado um menu semelhante a:

```text
=================================================
              CONVERSOR DE MOEDAS
=================================================

1 - Dólar
2 - Euro
3 - Iene
4 - Sair
```

O usuário escolhe a moeda desejada e informa o valor que deseja converter.

O sistema consulta a cotação através da API e apresenta o resultado no terminal.

---

## 📚 Conceitos praticados

Durante o desenvolvimento deste projeto estou praticando:

* Variáveis
* Tipos de dados
* Condicionais
* Loops
* Funções
* `return`
* Imports e módulos
* Dicionários
* Tratamento de exceções
* Requisições HTTP
* Métodos HTTP
* APIs REST
* JSON
* Manipulação de respostas de APIs
* Organização de projetos Python
* Git e GitHub

---

## 🚀 Próximas funcionalidades

O projeto continuará sendo desenvolvido.

### Planejado:

* [ ] Adicionar mais moedas
* [ ] Utilizar dicionários para eliminar repetição de código
* [ ] Melhorar o tratamento de erros da API
* [ ] Validar valores informados pelo usuário
* [ ] Permitir conversões entre diferentes moedas
* [ ] Criar histórico de conversões
* [ ] Melhorar a interface do terminal
* [ ] Aplicar Programação Orientada a Objetos
* [ ] Criar testes automatizados
* [ ] Criar uma API REST própria utilizando Flask
* [ ] Documentar os endpoints da API
* [ ] Melhorar o projeto para utilização no portfólio

---

## 🎯 Objetivo

O principal objetivo deste projeto é desenvolver conhecimento prático em **Python, APIs REST e desenvolvimento de software**, evoluindo gradualmente de um projeto simples de terminal para uma aplicação mais completa e estruturada.

---

## 👨‍💻 Autor

**Júlio César**

Estudante de Análise e Desenvolvimento de Sistemas.

Interesses:

* Python
* APIs REST
* Backend
* Flask
* MySQL
* Git e GitHub
* Desenvolvimento de Software

---

## 📈 Status do projeto

🚧 **Em desenvolvimento**

Este projeto está sendo desenvolvido continuamente como parte da minha jornada de aprendizado em desenvolvimento backend.
