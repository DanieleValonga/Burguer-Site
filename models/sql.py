import pymysql

# Conecte-se ao banco de dados

def execute(sql):
    conn = pymysql.connect(
        host="192.168.0.201",
        port=3306,
        database="dani",
        user="dani",
        password="Dani1234",
        cursorclass=pymysql.cursors.DictCursor,
    )

    with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


if __name__ == "__main__":
    print(
        execute(
            """SELECT burguer.name, GROUP_CONCAT(ingredient.name) as ingredients
FROM burguer
JOIN burgueringredients
ON	burguer.id = burgueringredients.burguer_id
JOIN ingredient
ON burgueringredients.ingredient_id = ingredient.id
	group by burguer.name;"""
        )
    )
