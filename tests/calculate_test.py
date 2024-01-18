from .utils.client import app, client

def test_calculate_x_burguer(client):
    response = client.post(
        "/api/v1.0/calculate",
        json={"name": "X-Burguer"},
    )
    expected = {
        "name": "X-Burguer",
        "OriginalPrice": 4.5,
        "promoPrice": 4.5,
        "promotions": [],
    }
    print(response.data)
    assert response.status_code == 200
    assert response.json == expected

def test_calculate_x_egg(client):
    response = client.post(
        "/api/v1.0/calculate",
        json={"name": "X-Egg"},
    )
    expected = {
        "name": "X-Egg",
        "OriginalPrice": 5.3,
        "promotionPrice": 5.3,
        "promotions": [],
    }
    
    print(response.data)
    assert response.status_code == 200
    assert response.json == expected
