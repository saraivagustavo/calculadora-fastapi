from fastapi import FastAPI, HTTPException
from services.operations import somar, subtrair, multiplicar, dividir
from models.models import OperacaoRequest, OperacaoResponse

app = FastAPI( #muda a apresentação da API
    title="FastAPI Calculadora",
    description="Uma API simples para operações matemáticas básicas usando FastAPI.",
    version="1.0.0"
)

requisicao_exemplo = { #exemplo de requisição que aparece na documentação da API
    "a": 10,
    "b": 20
}

######### SOMA #########
@app.post("/somar", response_model=OperacaoResponse, summary="Soma de dois números", response_description="Resultado da soma", tags=["Operações"])
async def somar_numeros(requisicao: OperacaoRequest):
    resultado = somar(requisicao.a, requisicao.b) #chama a função somar que está no services/operations.py
    return OperacaoResponse(resultado=resultado) #retorna a resposta no formato definido em OperacaoResponse que está no models/models.py, segue a mesma lógica do código do professor
#====================================


########## SUBTRAÇÃO #########
@app.post("/subtrair", response_model=OperacaoResponse, summary="Subtração de dois números", response_description="Resultado da subtração", tags=["Operações"])
async def subtrair_numeros(requisicao: OperacaoRequest):
    resultado = subtrair(requisicao.a, requisicao.b) #chama a função subtrair que está no services/operations.py
    return OperacaoResponse(resultado=resultado)
#====================================


########## MULTIPLICAÇÃO #########
@app.post("/multiplicar", response_model=OperacaoResponse, summary="Multiplicação de dois números", response_description="Resultado da multiplicação", tags=["Operações"])
async def multiplicar_numeros(requisicao: OperacaoRequest):
    resultado = multiplicar(requisicao.a, requisicao.b) #chama a função multiplicar que está no services/operations.py
    return OperacaoResponse(resultado=resultado)
#====================================


########## DIVISÃO #########
@app.post("/dividir", response_model=OperacaoResponse, summary="Divisão de dois números", response_description="Resultado da divisão", tags=["Operações"])
async def dividir_numeros(requisicao: OperacaoRequest):
    try: #tenta executar o código dentro do bloco try, se der erro, ele pula para o bloco except (mesma coisa de Orientação a Objetos)
        resultado = dividir(requisicao.a, requisicao.b) #chama a função dividir que está no services/operations.py
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) #erro 400: significa que a requisição feita pelo usuário é inválida, nesse caso, divisão por zero, o detail="" mostra a mensagem de erro se isso acontecer
    return OperacaoResponse(resultado=resultado)
