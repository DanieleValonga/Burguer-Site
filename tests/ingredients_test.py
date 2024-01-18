from app import ingredients


def test_ingredients_api(stub):

    output = ingredients()

    expected = {
        "Alface": 0.4,
        "Bacon": 2,
        "Hamburguer de Carne": 3,
        "Ovo": 0.8,
        "Queijo": 1.5,
    }

    print(output)

    assert output == expected
