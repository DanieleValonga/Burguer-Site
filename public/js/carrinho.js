const render_page = (carrinho) => {
    $("#container").empty()

    carrinho.sort((a, b) => {
        if(a.name < b.name) {
            return -1
        }

        if(a.name > b.name) {
            return 1
        }
        return 0
    }).forEach(element => {
        const name = element['name']
        const image = element['image']
        const price = element['price']
        const ingredients = element['ingredients']

        // const {name, image, price, ingredients} = element

        $("#container").append(`
            <tr id="${name}">
                <td><img src="${image}"></td>
                <td>${price.promoPrice}</td>
                <td>
                    <button id="botao-trash" class="material-symbols-outlined" onclick="removeItem('${name}')">delete</button>
                </td>
            </tr>
        `)
    });

}

$(document).ready(function() {
    $.ajax({
        url:`${host}/api/v1.0/carrinho`,
        method: "GET",
        headers: {"Authorization": "123"},
        success: function(data, status) {
            console.log(data)
            const carrinho = data['carrinho']
            render_page(carrinho)
        }
    })
})

const removeItem = (lancheName) => {
    $.ajax({
        url: `${host}/api/v1.0/carrinho`,
        method: "DELETE",
        headers: {
            "Authorization": "123",
            'Content-Type': 'application/json',
        },
        data: JSON.stringify({'name': lancheName}),
        success: (data) => {
            const carrinho = data['carrinho']
            console.log(carrinho)
            render_page(carrinho)
        }
    })
}

// const tabela = document.getElementById('tabela');
// const botaoTrash = document.getElementById('botao-trash');

// botaoTrash.addEventListener('click', () => {
//     if (botaoTrash.click) {
//         tabela.remove();
//     }
// });

function minhaFuncao() {
    alert("Olha! Você clicou em um botão que não faz bosta nenhuma. Ainda.")
}