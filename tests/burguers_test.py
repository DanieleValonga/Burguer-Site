from app import burguers


def test_burguers_api(stub):
    output = burguers()

    expected = {
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

    print(output)

    assert output == expected
