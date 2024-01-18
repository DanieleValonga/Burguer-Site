dados_json = {"name": "X-Burguer"}

price_ingredients = {
        "Alface": 0.4,
        "Bacon": 2,
        "Hamburguer de Carne": 3,
        "Ovo": 0.8,
        "Queijo": 1.5,
}
available_burguers = {
     "X-Bacon": {
            "ingredients": ["Bacon", "Hamburguer de Carne", "Queijo"],
            "image": "/public/images/x-bacon.png",
        },
        "X-Burguer": {
            "ingredients": ["Hamburguer de Carne", "Queijo"],
            "image": "/public/images/x-burger.png",
        },
        "X-Egg": {
            "ingredients": ["Ovo", "Hamburguer de Carne", "Queijo"],
            "image": "/public/images/x-egg.png",
        },
        "X-Egg Bacon": {
            "ingredients": ["Ovo", "Bacon", "Hamburguer de Carne", "Queijo"],
            "image": "/public/images/x-egg-bacon.png",
        },
}

expected = {
        "name": "X-Burguer",
        "OriginalPrice": 4.5,
        "promoPrice": 4.5,
        "promotions": [],
    }

name = dados_json.get('name', '')
choosen_burguer = available_burguers.get(name, {})
ingredients = choosen_burguer.get('ingredients', [])

# ---- faça o calculo dos ingredientes

soma = 0


for elemento in ingredients:
    if elemento in price_ingredients:
        soma = soma+price_ingredients[elemento]
    else:
        print("deu ruim!")
print(f"{soma}")

output = {
    "name": name,
    "OriginalPrice": soma,
    "promoPrice": soma,
    "promotions": [],
}

print(f"{output}")

assert output == expected
print('')

