# 🧮 Calculadora FastAPI

## Sobre o Projeto

Este projeto é uma **API de calculadora simples** desenvolvida utilizando o framework web **FastAPI**. Ele foi criado com o propósito educacional de explorar e consolidar os conceitos fundamentais do FastAPI, tornando-o um excelente recurso para desenvolvedores que estão aprendendo o framework.

Através desta calculadora, é possível demonstrar como:
*   Definir e gerenciar rotas de API.
*   Trabalhar com diferentes tipos de parâmetros (de caminho, de consulta e corpo da requisição).
*   Aproveitar a validação automática de dados fornecida pelo Pydantic.
*   Utilizar a documentação interativa (Swagger UI/ReDoc) que o FastAPI gera automaticamente.

## 🚀 Funcionalidades

A API oferece as quatro operações matemáticas básicas:

*   **Adição**
*   **Subtração**
*   **Multiplicação**
*   **Divisão**

## ✨ Conceitos do FastAPI Abordados

Este repositório é um playground prático para entender os seguintes aspectos do FastAPI:

*   **Definição de Rotas**: Utilização de decoradores como `@app.get()` e `@app.post()`.
*   **Parâmetros de Caminho (Path Parameters)**: Como extrair valores diretamente da URL (ex: `/subtract/{num1}/{num2}`).
*   **Parâmetros de Consulta (Query Parameters)**: Como receber dados através da string de consulta da URL (ex: `/add?num1=10&num2=5`).
*   **Corpo da Requisição (Request Body)**: Uso de modelos Pydantic para definir a estrutura e validar os dados enviados no corpo de requisições POST.
*   **Validação de Dados**: O poder do Pydantic para garantir que os dados recebidos estejam no formato e tipo corretos.
*   **Documentação Automática**: Exploração das interfaces Swagger UI (`/docs`) e ReDoc (`/redoc`) para testar e entender a API.
*   **Tratamento de Erros**: Como lidar com situações como divisão por zero.

## 🛠️ Tecnologias Utilizadas

*   **Python 3.x**
*   **FastAPI**: O framework web de alta performance.
*   **Uvicorn**: O servidor ASGI rápido que executa o FastAPI.
*   **Pydantic**: Biblioteca para validação de dados com tipagem Python.

## 💻 Como Rodar o Projeto

Siga os passos abaixo para configurar e executar a API da calculadora em sua máquina local.

### 1. Clonar o Repositório

Primeiro, clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/saraivagustavo/calculadora-fastapi.git
cd calculadora-fastapi
