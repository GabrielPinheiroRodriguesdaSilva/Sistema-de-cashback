# 💰 Calculadora de Cashback

Aplicação full stack que calcula cashback com base no tipo de cliente e valor da compra, armazenando histórico por IP.

---

## 🚀 Tecnologias utilizadas

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python com FastAPI
* **Banco de dados:** MySQL (Railway)
* **Deploy Backend:** Render
* **Deploy Frontend:** Netlify

---

## 📌 Funcionalidades

* ✔️ Cálculo de cashback em tempo real
* ✔️ Diferenciação por tipo de cliente (Normal / VIP)
* ✔️ Regras de cashback:

  * 5% padrão
  * +10% para clientes VIP
  * Dobro para compras acima de R$500
* ✔️ Registro de consultas por IP
* ✔️ Histórico individual por usuário

---

## 🌐 Acesse o projeto

🔗 **Frontend:**
https://cashback-gabriel.netlify.app/

🔗 **Backend (API):**
https://cashback-gabriel.onrender.com

🔗 **Documentação da API:**
https://cashback-gabriel.onrender.com/docs

---

## ⚙️ Como executar localmente

### 🔹 Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/Sistema-de-cashback.git
cd Sistema-de-cashback
```

---

### 🔹 Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 🔹 Rodar o backend

```bash
uvicorn main:app --reload
```

---

### 🔹 Abrir o frontend

Abra o arquivo `index.html` no navegador

---

## 🗄️ Estrutura do banco de dados

```sql
CREATE TABLE consultas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip VARCHAR(50),
    tipo VARCHAR(10),
    valor FLOAT,
    cashback FLOAT
);
```

---

## 📊 Endpoints da API

### 🔹 POST /cashback

Calcula cashback e registra no banco

**Exemplo de requisição:**

```json
{
  "tipo": "vip",
  "valor": 100
}
```

---

### 🔹 GET /historico

Retorna histórico de consultas por IP

---

## 👨‍💻 Autor

Desenvolvido por Gabriel Pinheiro 

---
