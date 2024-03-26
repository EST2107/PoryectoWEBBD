from flask import Flask , render_template , request,redirect, url_for,flash
from flask_mysqldb import MySQL





App = Flask(__name__) 

App.config['MYSQL_HOST']= 'localhost'
App.config['MYSQL_USER'] = 'root'
App.config['MYSQL_PASSWORD'] = 'password'
App.config['MYSQL_DB'] = 'Comideria3'
mysql = MySQL(App)

App.secret_key = 'mysecretkey'


@App.route('/')
def RegistroClientes():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM Clientes')
    data = cur.fetchall()
    print(data)    
    return render_template('RegistroClientes.html', Clientes = data)

@App.route('/RegistroPlatillos')
def RegistroPlatillos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Platillo')
    platillos = cur.fetchall()
    print(platillos)
    return render_template('RegistroPlatillos.html', platillos=platillos)






@App.route('/EditarPlatillo/<PlatilloID>')
def EditarPlatillo(PlatilloID):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Platillo WHERE PlatilloID = %s',(PlatilloID,))
    data = cur.fetchall()
    return render_template('EditarPlatillo.html',platillo = data [0])


@App.route('/ActualizarPlatillo/<int:PlatilloID>', methods=['POST'])
def ActualizarPlatillo(PlatilloID):
    if request.method == 'POST':
        nuevo_nombre = request.form['nuevo_nombre']
        nuevo_precio = request.form['nuevo_precio']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Platillo
            SET Nombre = %s,
                Precio = %s
            WHERE PlatilloID = %s
        """, (nuevo_nombre, nuevo_precio, PlatilloID))
        mysql.connection.commit()
        cur.close()

        flash('Platillo actualizado correctamente', 'success')
        return redirect(url_for('RegistroPlatillos'))


@App.route('/AgregarPlatillo', methods=['POST'])
def agregar_platillo():
    if request.method == 'POST':
        try:
            PlatilloID = request.form['PlatilloID']
            nombre = request.form['nombre']
            precio = request.form['precio']

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Platillo (PlatilloID, Nombre, Precio) VALUES (%s, %s, %s)", (PlatilloID, nombre, precio))
            mysql.connection.commit()
            cur.close()

            flash('Platillo agregado satisfactoriamente', 'success')
            return redirect(url_for('RegistroPlatillos'))

        except KeyError as e:
            return f'Error: {e}. Campo faltante en el formulario.'




@App.route('/EliminarPlatillo/<int:PlatilloID>', methods=['POST'])
def EliminarPlatillo(PlatilloID):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM Platillo WHERE PlatilloID = %s', (PlatilloID,))
        mysql.connection.commit()
        flash('EL PLATILLO HA SIDO ELIMINADO')
        return redirect(url_for('RegistroPlatillos'))






@App.route('/AgregarCliente/' , methods = ['POST'])
def AgregarContacto():
    if request.method == 'POST':
        try:
            Cedula = request.form['Cedula']
            Nombre = request.form['Nombre']
            Direccion = request.form['Direccion']
            Telefono = request.form['Telefono']

            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO Clientes (Cedula,Nombre,Direccion,Telefono) VALUES (%s,%s,%s,%s)',
                        (Cedula,Nombre,Direccion,Telefono))
            mysql.connection.commit()

            print(Cedula)
            print(Nombre)
            print(Direccion)
            print(Telefono)

            flash('CLIENTE AGREGADO SATISFACTORIAMENTE')
            return redirect(url_for('RegistroClientes'))
        
        except KeyError as e:
            return f'Error: {e}. Campo faltante en el formulario.'



@App.route('/EditarCliente/<Cedula>')
def EditarCliente(Cedula):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Clientes WHERE Cedula = %s',(Cedula,))
    data = cur.fetchall()
    return render_template('EditarCliente.html',Cliente = data [0])
   

@App.route('/Actualizar/<Cedula>', methods=['POST'])
def ActualizarCliente(Cedula):
  if request.method == 'POST':

        Cedula_nueva = request.form['Cedula'] 
        Nombre = request.form['Nombre']
        Direccion = request.form['Direccion']
        Telefono = request.form['Telefono']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Clientes
            SET Cedula = %s,
                Nombre = %s,
                Direccion = %s,
                Telefono = %s
            WHERE Cedula = %s 
        """, (Cedula_nueva, Nombre, Direccion, Telefono, Cedula))
        mysql.connection.commit()
        flash('CLIENTE ACTUALIZADO CORRECTAMENTE')
        return redirect(url_for('RegistroClientes'))


@App.route('/EliminarCliente/<string:Cedula>')
def EliminarCliente(Cedula):
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM Clientes WHERE Cedula = %s', (Cedula,))
        mysql.connection.commit()
        flash('EL CLIENTE HA SIDO ELIMINADO')
        return redirect(url_for('RegistroClientes'))




if __name__ == '__main__':
    App.run(port = 3000, debug = True)



