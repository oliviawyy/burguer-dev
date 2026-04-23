function mostrar_carrinho() {
    const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho")

    if (!resposta.ok) {
        alert("ERRO AO CARREGAR O CARRINHO!")
    }
    else {
        const dados = await resposta.json()

        const carrinho = document.getElementById("carrinho")

        carrinho.innerHTML = "";

        let total = 0;

        for (let dado of dados) {
            total += dado.preco;
            let linha = `<div class="cart-item">
          <img src="${dado.imagem}" alt="Hambúrguer Clássico" class="cart-item__img" />
          <div class="cart-item__details">
            <h3 class="cart-item__name">${dado.nome}</h3>
            <p class="cart-item__price">${dado.preco}</p>
          </div>
          <button class="cart-item__remove">Remover</button>
        </div>`

            carrinho.innerHTML += linha;
        }
    }
}


mostrarCarrinho