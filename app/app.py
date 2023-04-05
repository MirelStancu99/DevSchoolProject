# Importăm bibliotecile necesare
from flask import Flask, render_template, request, jsonify
import socket
import sqlite3
import os
import requests
# Inițializăm aplicația Flask
app = Flask(__name__)


#DATABASE
# connection = sqlite3.connect('database.db')
#Verificam daca db/database.db este populata,daca nu, o populam
# if( os.path.isfile('database.db') and os.path.getsize('database.db') == 0 ):
#     with open('schema.sql') as f:
#         connection.executescript(f.read())

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Pentru hostname,ip section
def fetchAddressDetail():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip)
    

# Definim ruta pentru afișarea datelor despre alimente
@app.route('/')
def home():
    #MAIN BARS
    hostname,ip = fetchAddressDetail()

    conn = get_db_connection()
    maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    total_foods = str(resultFoodsCounter[0])
    maxResult = maxCalories["denumire"]
    minResult = minCalories["denumire"]
    
    conn.close()

    return render_template('index.html', HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult,MINCALORIES=minResult, TOTALALIMENTE=total_foods)

@app.route('/foods')
def foods():

    #MAIN BARS
    hostname,ip = fetchAddressDetail()

    conn = get_db_connection()
    #EXCLUSIVE FOR FOODS
    foods = conn.execute('SELECT * FROM foods').fetchall()
    #--------------------------------
    maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    total_foods = str(resultFoodsCounter[0])
    maxResult = maxCalories["denumire"]
    minResult = minCalories["denumire"]
    
    conn.close()
    return render_template('foods.html', foods=foods, HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult,MINCALORIES=minResult, TOTALALIMENTE=total_foods)

@app.route('/lowCalories')
def foodsR():
    hostname,ip = fetchAddressDetail()


    conn = get_db_connection()
    maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    total_foods = str(resultFoodsCounter[0])
    maxResult = maxCalories["denumire"]
    minResult = minCalories["denumire"]
    foods = conn.execute('SELECT * FROM foods WHERE calorii < 400 ORDER BY calorii DESC').fetchall()
    conn.close()
    return render_template('lowCalories.html', foods=foods, HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult,MINCALORIES=minResult, TOTALALIMENTE=total_foods)

@app.route('/addFood')
def addFood():
    #MAIN BARS
    hostname,ip = fetchAddressDetail()

    conn = get_db_connection()
    maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    total_foods = str(resultFoodsCounter[0])
    maxResult = maxCalories["denumire"]
    minResult = minCalories["denumire"]
    conn.close()
    return render_template('addFood.html', HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult,MINCALORIES=minResult, TOTALALIMENTE=total_foods)

def check_food_name(name):
    conn = get_db_connection()
    result = conn.execute('SELECT * FROM foods WHERE denumire = ?', (name,)).fetchone()
    conn.close()

    if result is None:
        return False
    else:
        return True
    
@app.route('/proceseaza_formular', methods=['POST'])
def proceseaza_formular():
    # Primim datele din formular
    denumire = str(request.form['denumire']).strip()
    numar_de_calorii = request.form['numar_de_calorii']
    proteine = request.form['proteine']
    gramaj = 100
    # Validăm datele

    exista = check_food_name(denumire)

    if not denumire:
        mesaj_eroare = "Denumirea nu poate fi goală."
    elif exista:
        mesaj_eroare = "Produsul exista deja in baza de date."
    elif not numar_de_calorii.isdigit() or not proteine.isdigit():
        mesaj_eroare = "Numărul de calorii și proteine trebuie să fie numere întregi pozitive."
    else:
        # Datele sunt valide
        # Salvăm datele în baza de date
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO foods (denumire, calorii, proteine, gramaj) VALUES (?, ?, ?,?)", (denumire, numar_de_calorii, proteine,gramaj))
        conn.commit()
        hostname,ip = fetchAddressDetail()
        maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
        minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
        resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
        total_foods = str(resultFoodsCounter[0])
        maxResult = maxCalories["denumire"]
        minResult = minCalories["denumire"]
        foods = conn.execute('SELECT * FROM foods').fetchall()
        conn.close()
        # Afișăm mesajul de succes către utilizator
        mesaj_succes = "Alimentul a fost adăugat cu succes."
        return render_template('rezultat.html', MESAJ_SUCCES=mesaj_succes ,foods=foods, HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult, MINCALORIES=minResult, TOTALALIMENTE=total_foods)
    
    #MAIN BARS
    hostname,ip = fetchAddressDetail()

    conn = get_db_connection()
    maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    total_foods = str(resultFoodsCounter[0])
    maxResult = maxCalories["denumire"]
    minResult = minCalories["denumire"]
    
    conn.close()
    # Afișăm mesajul de eroare către utilizator
    return render_template('addFood.html', MESAJ_EROARE=mesaj_eroare, HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult,MINCALORIES=minResult, TOTALALIMENTE=total_foods)

def check_food_id(id):
    conn = get_db_connection()
    result = conn.execute('SELECT * FROM foods WHERE id = ?', (id,)).fetchone()
    conn.close()

    if result is None:
        return False
    else:
        return True
    
@app.route('/deleteFood')
def deleteFood():
    #MAIN BARS
    hostname,ip = fetchAddressDetail()

    conn = get_db_connection()
    #EXCLUSIVE FOR FOODS
    foods = conn.execute('SELECT * FROM foods').fetchall()
    #--------------------------------
    maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    total_foods = str(resultFoodsCounter[0])
    maxResult = maxCalories["denumire"]
    minResult = minCalories["denumire"]
    
    conn.close()
    return render_template('deleteFood.html', foods=foods, HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult,MINCALORIES=minResult, TOTALALIMENTE=total_foods)

@app.route('/proceseaza_stergere', methods=['POST'])
def proceseaza_stergere():
    # Primim datele din formular
    id = request.form['id']

    # Validăm datele

    exista = check_food_id(id)

    
    if not id.isdigit():
        mesaj_eroare = "ID ul trebuie sa fie numar si sa fie pozitiv."
    elif not exista:
        mesaj_eroare = "Produsul nu exista."
    else:
        # Datele sunt validePOST
        # Salvăm datele în baza de date
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM foods WHERE id = ?", (id,))
        conn.commit()
        foods = conn.execute('SELECT * FROM foods').fetchall()
        hostname,ip = fetchAddressDetail()
        maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
        minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
        resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
        total_foods = str(resultFoodsCounter[0])
        maxResult = maxCalories["denumire"]
        minResult = minCalories["denumire"]
        conn.close()
        # Afișăm mesajul de succes către utilizator
        mesaj_succes = "Alimentul a fost sters cu succes."
        return render_template('rezultat.html', MESAJ_SUCCES=mesaj_succes ,foods=foods, HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult, MINCALORIES=minResult, TOTALALIMENTE=total_foods)
    
    # Afișăm mesajul de eroare către utilizator
    #MAIN BARS
    hostname,ip = fetchAddressDetail()

    conn = get_db_connection()
    #EXCLUSIVE FOR FOODS
    foods = conn.execute('SELECT * FROM foods').fetchall()
    #--------------------------------
    maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    total_foods = str(resultFoodsCounter[0])
    maxResult = maxCalories["denumire"]
    minResult = minCalories["denumire"]
    
    conn.close()
    return render_template('deleteFood.html', MESAJ_EROARE=mesaj_eroare, foods=foods, HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult,MINCALORIES=minResult, TOTALALIMENTE=total_foods)

@app.route('/contact')
def contact():
    #MAIN BARS
    hostname,ip = fetchAddressDetail()

    conn = get_db_connection()
    maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    total_foods = str(resultFoodsCounter[0])
    maxResult = maxCalories["denumire"]
    minResult = minCalories["denumire"]
    
    conn.close()

    return render_template('contact.html', HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult,MINCALORIES=minResult, TOTALALIMENTE=total_foods)

@app.route('/liveness')
def liveness():
    #MAIN BARS
    hostname,ip = fetchAddressDetail()

    conn = get_db_connection()
    maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    total_foods = str(resultFoodsCounter[0])
    maxResult = maxCalories["denumire"]
    minResult = minCalories["denumire"]
    
    conn.close()

    api_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(api_url)
    if response.status_code == 200:
        responseSTR = "API is alive"
        color = "#c8e6c9"
    else:
        responseSTR = "API is down"
        color = "red"
    return render_template('liveness.html',COLOR = color,RESPONSE = responseSTR,HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult,MINCALORIES=minResult, TOTALALIMENTE=total_foods)

@app.route('/api')
def api():
    #MAIN BARS
    hostname,ip = fetchAddressDetail()

    conn = get_db_connection()
    maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    total_foods = str(resultFoodsCounter[0])
    maxResult = maxCalories["denumire"]
    minResult = minCalories["denumire"]
    
    conn.close()

    api_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(api_url)
    responses = response.json()  # Parsați JSON-ul într-un obiect Python
    
    return render_template('api.html',responses = responses,HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult,MINCALORIES=minResult, TOTALALIMENTE=total_foods)

@app.route('/apiOrdonat')
def apiOrdonat():
    #MAIN BARS
    hostname,ip = fetchAddressDetail()

    conn = get_db_connection()
    maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    total_foods = str(resultFoodsCounter[0])
    maxResult = maxCalories["denumire"]
    minResult = minCalories["denumire"]
    
    conn.close()

    # with open('users.json') as f:
    # responses = json.load(f)
    api_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(api_url)
    responses = response.json()  # Parsați JSON-ul într-un obiect Python
    responses = sorted(responses, key=lambda k: k['name'])
    
    return render_template('apiOrdonat.html',responses = responses,HOSTNAME = hostname, IP = ip, MAXCALORIES=maxResult,MINCALORIES=minResult, TOTALALIMENTE=total_foods)

# Rulăm aplicația pe localhost, portul 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
