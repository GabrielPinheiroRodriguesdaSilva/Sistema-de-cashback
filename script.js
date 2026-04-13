async function calcular(){

let tipo = document.getElementById("tipo").value
let valor = document.getElementById("valor").value

let response = await fetch("https://Cashback-Gabriel.onrender.com/cashback", {

method: "POST",

headers: {
"Content-Type": "application/json"
},

body: JSON.stringify({
tipo: tipo,
valor: valor
})

})

let data = await response.json()

document.getElementById("resultado").innerText =
"Cashback: R$ " + data.cashback

carregarHistorico()

}


async function carregarHistorico(){

let response = await fetch("https://Cashback-Gabriel.onrender.com/historico")

let dados = await response.json()

let lista = document.getElementById("historico")

lista.innerHTML = ""

dados.forEach(item => {

let li = document.createElement("li")

li.innerText =
`Tipo: ${item.tipo} | Valor: R$ ${item.valor} | Cashback: R$ ${item.cashback}`

lista.appendChild(li)

})

}

carregarHistorico()