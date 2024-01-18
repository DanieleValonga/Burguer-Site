from flask import Flask, render_template, request, jsonify, make_response
# from models.sql import execute as db
from tests.utils.stubs import mysql_stub as db
from uuid import uuid4 as generate_session_id

app = Flask(__name__, template_folder='template', static_folder='public')

session = {}

#---Pages---

@app.route('/')
def home():
    session_id = request.cookies.get('session_id', str(generate_session_id()))

    resp = make_response(render_template("jinja_main.html"))
    resp.set_cookie('session_id', session_id)

    return resp

@app.route('/carrinho')
def carrinho():
    return render_template('jinja_carrinho.html')

@app.route('/itens')
def itens():
    return render_template('jinja_itens.html')

#---APIs---

@app.route('/api/v1.0/burgers')
def burguers():
    results = db("""SELECT burguer.name, burguer.image, GROUP_CONCAT(ingredient.name) as ingredients
                    FROM burguer
                    JOIN burgueringredients
                    ON	burguer.id = burgueringredients.burguer_id
                    JOIN ingredient
                    ON burgueringredients.ingredient_id = ingredient.id
	group by burguer.name, burguer.image;""")

    output = {}

    for linha in results:
        name = linha['name']
        image = linha["image"]
        ingredients = linha['ingredients'].split(',')

        output[name] = {
            'ingredients': ingredients,
            'image': image
        }

    return output

@app.route('/api/v1.0/ingredients')
def ingredients():
    results = db("SELECT * from ingredient")

    output = {}

    for linha in results:
        name = linha['name']
        price = linha['price']

        output[name] = price

    return output

@app.route("/api/v1.0/calculate", methods=
["POST"])
def calculate():
    dados_json = request.get_json()
    price_ingredients = ingredients()
    available_burguers = burguers()

    name = dados_json.get('name', '')
    choosen_burguer = available_burguers.get(name, {})
    current_ingredients = choosen_burguer.get('ingredients', [])

    # ---- faça o calculo dos ingredientes

    soma = 0

    for elemento in current_ingredients:
        if elemento in price_ingredients:
            soma = soma+price_ingredients[elemento]
        else:
            print("deu ruim!")
    print(f"{soma}")

    output = {
        "name": name,
        "originalPrice": soma,
        "promoPrice": soma,
        "promotions": [],
    }

    return jsonify(output)

@app.route("/api/v1.0/carrinho", methods=["POST", "GET", "DELETE"])
def session_carrinho():
    session_id = request.cookies.get('session_id', None)

    user_session = session.get(session_id, {})
    carrinho = user_session.get('carrinho', [])

    if request.method == 'GET':
        return jsonify({'carrinho': carrinho}), 200

    elif request.method == 'POST':
        new_item = request.get_json()

        carrinho.append(new_item)
        user_session['carrinho'] = carrinho
        session[session_id] = user_session

        return jsonify({}), 201
    elif request.method == 'DELETE':
        item_to_remove = request.get_json()
        name = item_to_remove['name']
        for idx, item in enumerate(carrinho):
            if item['name'] == name:
                carrinho.pop(idx)
                return jsonify({'carrinho': carrinho}), 200
        return jsonify({'carrinho': carrinho}), 404
    return {}



if __name__ == '__main__':
    app.run(debug=True)