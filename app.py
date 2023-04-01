# Importăm bibliotecile necesare
from flask import Flask, render_template
import json

# Inițializăm aplicația Flask
app = Flask(__name__)

# Definim ruta pentru afișarea datelor despre alimente
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/foods')
def foods():
    with open('data.json', 'r') as f:
        foods = json.load(f)
    return render_template('foods.html', foods=foods)

@app.route('/foodsR')
def foodsR():
    with open('data.json', 'r') as f:
        foods = json.load(f)
    sorted_foods = sorted(foods, key=lambda x: x['numar_de_calorii'], reverse=True)
    return render_template('foodsR.html', foods=sorted_foods)

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Rulăm aplicația pe localhost, portul 5000
if __name__ == '__main__':
    app.run(debug=True)
