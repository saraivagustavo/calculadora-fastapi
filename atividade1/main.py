from fastapi import FastAPI, HTTPException
from services.operations import *
from models.models import OperacaoRequest, OperacaoResponse

app = FastAPI(
    title="API de Operações Matemáticas",
    description="Uma API simples para realizar operações matemáticas básicas como soma, subtração, multiplicação e divisão.",
    version="1.0.0"
)

@app.get("/", summary="Página inicial", response_description="Mensagem de boas-vindas")
async def read_root():
    return {"message": "Bem-vindo à API de Operações Matemáticas!"}


######### SOMA #########
@app.post("/somar", response_model=OperacaoResponse, summary="Soma de dois números", response_description="Resultado da soma", tags=["Operações"])
async def somar_numeros(requisicao: OperacaoRequest): #os parâmetros da função são definidos pelo modelo OperacaoRequest 
    resultado = somar(requisicao.a, requisicao.b) #chama a função somar que está no services/operations.py
    return OperacaoResponse(resultado=resultado) #retorna a resposta no formato definido em OperacaoResponse
#====================================


########## SUBTRAÇÃO #########
@app.post("/subtrair", response_model=OperacaoResponse, summary="Subtração de dois números", response_description="Resultado da subtração", tags=["Operações"])
async def subtrair_numeros(requisicao: OperacaoRequest): #mesma lógica da soma
    resultado = subtrair(requisicao.a, requisicao.b) #chama a função subtrair que está no services/operations.py
    return OperacaoResponse(resultado=resultado) #mesma lógica da soma
#====================================


########## MULTIPLICAÇÃO #########
@app.post("/multiplicar", response_model=OperacaoResponse, summary="Multiplicação de dois números", response_description="Resultado da multiplicação", tags=["Operações"])
async def multiplicar_numeros(requisicao: OperacaoRequest): #mesma lógica da soma
    resultado = multiplicar(requisicao.a, requisicao.b) #chama a função multiplicar que está no services/operations.py
    return OperacaoResponse(resultado=resultado) #mesma lógica da soma
#====================================


########## DIVISÃO #########
@app.post("/dividir", response_model=OperacaoResponse, summary="Divisão de dois números", response_description="Resultado da divisão", tags=["Operações"])
async def dividir_numeros(requisicao: OperacaoRequest): #mesma lógica da soma
    try: #tenta executar o código dentro do bloco try, se der erro, ele pula para o bloco except (msm coisa de poo)
        resultado = dividir(requisicao.a, requisicao.b) #chama a função dividir que está no services/operations.py
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) #erro 400: significa que a requisição feita pelo usuário é inválida, nesse caso, divisão por zero, o detail="" mostra a mensagem de erro se isso acontecer
    return OperacaoResponse(resultado=resultado) #mesma lógica da soma
