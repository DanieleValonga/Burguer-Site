from flask import Flask, render_template

app = Flask(__name__, template_folder='template', static_folder='public')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/adicionais')
def adicionais():
    return render_template('adicionais.html')

if __name__ == '__main__':
    app.run()