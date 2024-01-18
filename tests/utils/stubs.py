from pytest_stub.toolbox import stub_global


def burguers_results():
    print("STUBBED")
    return [
        {
            "ingredients": "Bacon,Hamburguer de Carne,Queijo",
            "name": "X-Bacon",
            "image": "/public/images/x-bacon.png",
        },
        {
            "ingredients": "Hamburguer de Carne,Queijo",
            "name": "X-Burguer",
            "image": "/public/images/x-burger.png",
        },
        {
            "ingredients": "Ovo,Hamburguer de Carne,Queijo",
            "name": "X-Egg",
            "image": "/public/images/x-egg.png",
        },
        {
            "ingredients": "Ovo,Bacon,Hamburguer de Carne,Queijo",
            "name": "X-Egg Bacon",
            "image": "/public/images/x-egg-bacon.png",
        },
    ]


def ingredients_results():
    print("STUBBED")
    return [
        {"price": 0.4, "name": "Alface"},
        {"price": 2.0, "name": "Bacon"},
        {"price": 3.0, "name": "Hamburguer de Carne"},
        {"price": 0.8, "name": "Ovo"},
        {"price": 1.5, "name": "Queijo"},
    ]


def mysql_stub(sql):
    if (
        sql
        == """SELECT burguer.name, burguer.image, GROUP_CONCAT(ingredient.name) as ingredients
                    FROM burguer
                    JOIN burgueringredients
                    ON	burguer.id = burgueringredients.burguer_id
                    JOIN ingredient
                    ON burgueringredients.ingredient_id = ingredient.id
	group by burguer.name, burguer.image;"""
    ):
        return burguers_results()
    elif sql == "SELECT * from ingredient":
        return ingredients_results()
    else:
        return []


stub_global(
    {
        "models.sql.execute": mysql_stub,
    }
)
