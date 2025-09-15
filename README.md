# 🧮 Calculadora FastAPI

## Sobre o Projeto

Este projeto é uma **API de calculadora simples** desenvolvida
utilizando o framework web **FastAPI**. Ele foi criado com o propósito
educacional de explorar e consolidar os conceitos fundamentais do
FastAPI, tornando-o um excelente recurso para desenvolvedores que estão
aprendendo o framework.

Através desta calculadora, é possível demonstrar como: \* Definir e
gerenciar rotas de API. \* Trabalhar com diferentes tipos de parâmetros
(de caminho, de consulta e corpo da requisição). \* Aproveitar a
validação automática de dados fornecida pelo Pydantic. \* Utilizar a
documentação interativa (Swagger UI/ReDoc) que o FastAPI gera
automaticamente.

## 🚀 Funcionalidades

A API oferece as quatro operações matemáticas básicas:

-   **Adição**
-   **Subtração**
-   **Multiplicação**
-   **Divisão**

## ✨ Conceitos do FastAPI Abordados

Este repositório é um playground prático para entender os seguintes
aspectos do FastAPI:

-   **Definição de Rotas**: Utilização de decoradores como `@app.get()`
    e `@app.post()`.
-   **Parâmetros de Caminho (Path Parameters)**: Como extrair valores
    diretamente da URL (ex: `/subtract/{num1}/{num2}`).
-   **Parâmetros de Consulta (Query Parameters)**: Como receber dados
    através da string de consulta da URL (ex: `/add?num1=10&num2=5`).
-   **Corpo da Requisição (Request Body)**: Uso de modelos Pydantic para
    definir a estrutura e validar os dados enviados no corpo de
    requisições POST.
-   **Validação de Dados**: O poder do Pydantic para garantir que os
    dados recebidos estejam no formato e tipo corretos.
-   **Documentação Automática**: Exploração das interfaces Swagger UI
    (`/docs`) e ReDoc (`/redoc`) para testar e entender a API.
-   **Tratamento de Erros**: Como lidar com situações como divisão por
    zero.

## 🛠️ Tecnologias Utilizadas

-   **Python 3.x**
-   **FastAPI**: O framework web de alta performance.
-   **Uvicorn**: O servidor ASGI rápido que executa o FastAPI.
-   **Pydantic**: Biblioteca para validação de dados com tipagem Python.

## 💻 Como Rodar o Projeto

Siga os passos abaixo para configurar e executar a API da calculadora em
sua máquina local.

### 1. Clonar o Repositório

Primeiro, clone o repositório para o seu ambiente local:

``` bash
git clone https://github.com/saraivagustavo/calculadora-fastapi.git
cd calculadora-fastapi
```

### 2. Criar e Ativar um Ambiente Virtual (Recomendado)

É uma boa prática isolar as dependências do projeto em um ambiente
virtual:

``` bash
python -m venv venv
# Para Windows
.env\Scriptsctivate
# Para macOS/Linux
source venv/bin/activate
```

### 3. Instalar as Dependências

Instale as bibliotecas necessárias. Se você ainda não tem um
requirements.txt, pode instalá-las diretamente:

``` bash
pip install fastapi uvicorn
# Ou, se já tiver um requirements.txt:
# pip install -r requirements.txt
```

### 4. Executar a Aplicação

Inicie o servidor FastAPI usando Uvicorn. O --reload é útil para
desenvolvimento, pois o servidor reiniciará automaticamente a cada
mudança no código.

``` bash
uvicorn main:app --reload
```

A API estará agora acessível em http://127.0.0.1:8000.

## 🔬 Uso da API

Com o servidor em execução, você pode acessar as interfaces de
documentação interativa para testar os endpoints:

-   **Swagger UI:** http://127.0.0.1:8000/docs
-   **ReDoc:** http://127.0.0.1:8000/redoc

### Exemplos de uso:

#### Adição (GET com Query Parameters)

-   **Endpoint:** `/add`
-   **Exemplo:** http://127.0.0.1:8000/add?num1=10&num2=5\
-   **Resposta esperada:** `{"resultado": 15}`

#### Subtração (GET com Path Parameters)

-   **Endpoint:** `/subtract/{num1}/{num2}`
-   **Exemplo:** http://127.0.0.1:8000/subtract/10/5\
-   **Resposta esperada:** `{"resultado": 5}`

#### Multiplicação (POST com Request Body)

-   **Endpoint:** `/multiply`
-   **Método:** POST\
-   **Corpo da Requisição (JSON):**

``` json
{
  "num1": 10,
  "num2": 5
}
```

-   **Resposta esperada:** `{"resultado": 50}`

#### Divisão (GET com Query Parameters e Tratamento de Erro)

-   **Endpoint:** `/divide`
-   **Exemplo:** http://127.0.0.1:8000/divide?num1=10&num2=2\
-   **Resposta esperada:** `{"resultado": 5.0}`

**Exemplo de erro (divisão por zero):**\
http://127.0.0.1:8000/divide?num1=10&num2=0\
Resposta de erro esperada:
`{"detail": "Não é possível dividir por zero."}`

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Se você tiver sugestões de
melhoria, novas funcionalidades para adicionar ou quiser corrigir algum
bug, sinta-se à vontade para:

1.  Fazer um "fork" do projeto.
2.  Criar uma nova branch: `git checkout -b feature/sua-nova-feature`.
3.  Realizar suas alterações e commitá-las:
    `git commit -m 'Adiciona [sua alteração]'`.
4.  Fazer push para a sua branch:
    `git push origin feature/sua-nova-feature`.
5.  Abrir um Pull Request detalhando suas mudanças.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Para mais detalhes,
consulte o arquivo LICENSE na raiz do repositório (se disponível).
