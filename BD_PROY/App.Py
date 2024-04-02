from flask import Flask , render_template , request,redirect, url_for,flash,jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS





app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'Comideria3'
mysql = MySQL(app)


@app.route('/servidor', methods=['POST'])
def recibir_datos():
    data = request.json  
    print("Datos recibidos:", data)
    response = {"message": "Datos recibidos correctamente"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=3000)

