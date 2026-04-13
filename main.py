from fastapi import FastAPI, Request
from pydantic import BaseModel
import pymysql

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (libera acesso do frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de dados
class Dados(BaseModel):
    tipo: str
    valor: float


# 🔥 Conexão com MySQL (Railway)
def get_connection():
    return pymysql.connect(
        host="monorail.proxy.rlwy.net",
        user="root",
        password="vJLZAigDUmWOeGZYjfdYuCTPqvHqluSf",
        database="railway",
        port=39885,
        ssl={"ssl": {}}
    )


# 💰 Regra de cashback
def calcular_cashback(valor, tipo):
    cashback = valor * 0.05

    if tipo.lower() == "vip":
        cashback *= 1.10

    if valor > 500:
        cashback *= 2

    return round(cashback, 2)


# 📌 Endpoint para calcular cashback
@app.post("/cashback")
async def cashback(dados: Dados, request: Request):
    tipo = dados.tipo
    valor = dados.valor
    ip = request.client.host

    cashback = calcular_cashback(valor, tipo)

    con = get_connection()
    cursor = con.cursor()

    try:
        sql = """
        INSERT INTO consultas (ip, tipo, valor, cashback)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (ip, tipo, valor, cashback))
        con.commit()
    finally:
        cursor.close()
        con.close()

    return {"cashback": cashback}


# 📊 Endpoint de histórico
@app.get("/historico")
async def historico(request: Request):
    ip = request.client.host

    con = get_connection()
    cursor = con.cursor()

    try:
        sql = "SELECT tipo, valor, cashback FROM consultas WHERE ip=%s"
        cursor.execute(sql, (ip,))
        dados = cursor.fetchall()
    finally:
        cursor.close()
        con.close()

    # 🔥 retorna em JSON organizado
    return [
        {
            "tipo": d[0],
            "valor": float(d[1]),
            "cashback": float(d[2])
        }
        for d in dados
    ]