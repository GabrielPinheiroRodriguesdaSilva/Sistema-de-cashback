from fastapi import FastAPI, Request
from pydantic import BaseModel
import pymysql

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Dados(BaseModel):
    tipo: str
    valor: float


def get_connection():
    return pymysql.connect(
        host="mysql.railway.internal",
        user="root",
        password="vJLZAigDUmWOeGZYjfdYuCTPqvHqluSf",
        database="railway",
        port=3306
        ssl={"ssl": {}}
    )


def calcular_cashback(valor, tipo):

    valor_final = valor

    cashback = valor_final * 0.05

    if tipo.lower() == "vip":
        cashback *= 1.10
 
    if valor_final > 500:
        cashback *= 2

    return round(cashback, 2)


@app.post("/cashback")
async def cashback(dados: Dados, request: Request):

    tipo = dados.tipo
    valor = dados.valor

    ip = request.client.host

    cashback = calcular_cashback(valor, tipo)

    cursor = con.cursor()

    sql = """
    INSERT INTO consultas (ip, tipo, valor, cashback)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(sql, (ip, tipo, valor, cashback))
    con.commit()

    return {
        "cashback": cashback
    }


@app.get("/historico")
async def historico(request: Request):

    ip = request.client.host

    cursor = con.cursor()

    sql = "SELECT tipo, valor, cashback FROM consultas WHERE ip=%s"

    cursor.execute(sql, (ip,))

    dados = cursor.fetchall()

    return [
    {
        "tipo": d[0],
        "valor": float(d[1]),
        "cashback": float(d[2])
    }
    for d in dados
]