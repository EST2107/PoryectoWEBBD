from flask import Flask , render_template , request,redirect, url_for,flash
from flask_mysqldb import MySQL





App = Flask(__name__) 

App.config['MYSQL_HOST']= 'localhost'
App.config['MYSQL_USER'] = 'root'
App.config['MYSQL_PASSWORD'] = 'Gokussjblue123KEVIN.'
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

@App.route('/RegistroProveedores')
def RegistroProveedores():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Proveedores')
    proveedores = cur.fetchall()
    print(proveedores)  
    return render_template('RegistroProveedores.html', proveedores=proveedores)




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

            
            return redirect(url_for('RegistroPlatillos'))

        except KeyError as e:
            return f'Error: {e}. Campo faltante en el formulario.'




@App.route('/EliminarPlatillo/<int:PlatilloID>', methods=['POST'])
def EliminarPlatillo(PlatilloID):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM Platillo WHERE PlatilloID = %s', (PlatilloID,))
        mysql.connection.commit()
        
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


@App.route('/EliminarProveedor/<int:ProveedorID>')
def EliminarProveedor(ProveedorID):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Proveedores WHERE ProveedorID = %s', (ProveedorID,))
    mysql.connection.commit()
   
    return redirect(url_for('RegistroProveedores'))



@App.route('/AgregarProveedor', methods=['POST'])
def AgregarProveedor():
    if request.method == 'POST':
        try:
            ProveedorID = request.form['ProveedorID']
            Nombre = request.form['Nombre']
            Direccion = request.form['Direccion']
            Telefono = request.form['Telefono']

            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO Proveedores (ProveedorID, Nombre, Direccion, Telefono) VALUES (%s, %s, %s, %s)',
                        (ProveedorID, Nombre, Direccion, Telefono))
            mysql.connection.commit()

           
            return redirect(url_for('RegistroProveedores'))
        
        except KeyError as e:
            return f'Error: {e}. Campo faltante en el formulario.'
        
        


@App.route('/EliminarCliente/<string:Cedula>')
def EliminarCliente(Cedula):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Clientes WHERE Cedula = %s', (Cedula,))
    mysql.connection.commit()
    flash('EL CLIENTE HA SIDO ELIMINADO')
    return redirect(url_for('RegistroClientes'))




@App.route('/EditarProveedor/<string:ProveedorID>')
def EditarProveedor(ProveedorID):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Proveedores WHERE ProveedorID = %s', (ProveedorID,))
    proveedor = cur.fetchone()
    cur.close()
    return render_template('EditarProveedor.html', proveedor=proveedor)



@App.route('/ActualizarProveedor/<string:ProveedorID>', methods=['POST'])
def ActualizarProveedor(ProveedorID):
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Proveedores
            SET Nombre = %s,
                Direccion = %s,
                Telefono = %s
            WHERE ProveedorID = %s
        """, (nombre, direccion, telefono, ProveedorID))
        mysql.connection.commit()
      
        return redirect(url_for('RegistroProveedores'))


@App.route('/RegistroProductos')
def RegistroProductos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Productos')
    productos = cur.fetchall()
    return render_template('RegistroProductos.html', productos=productos)



@App.route('/AgregarProducto', methods=['POST'])
def AgregarProducto():
    if request.method == 'POST':
        try:
            ProductoID = request.form['ProductoID']
            Nombre = request.form['Nombre']
            Cantidad = request.form['Cantidad']

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Productos (ProductoID, Nombre, CantidadDisponible) VALUES (%s, %s, %s)", (ProductoID,Nombre,Cantidad))
            mysql.connection.commit()
            cur.close()

        
            return redirect(url_for('RegistroProductos'))

        except KeyError as e:
            return f'Error: {e}. Campo faltante en el formulario.'

@App.route('/EliminarProducto/<int:ProductoID>', methods=['POST'])
def EliminarProducto(ProductoID):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM Productos WHERE ProductoID = %s', (ProductoID,))
        mysql.connection.commit()
       
        return redirect(url_for('RegistroProductos'))


@App.route('/EditarProducto/<int:ProductoID>', methods=['GET'])
def EditarProducto(ProductoID):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Productos WHERE ProductoID = %s', (ProductoID,))
    producto = cur.fetchone()
    cur.close()
    return render_template('EditarProducto.html', producto=producto)


@App.route('/ActualizarProducto/<int:ProductoID>', methods=['POST'])
def ActualizarProducto(ProductoID):
    if request.method == 'POST':
        try:
            Nombre = request.form['Nombre']
            Cantidad = request.form['Cantidad']

            cur = mysql.connection.cursor()
            cur.execute("""
                UPDATE Productos
                SET Nombre = %s,
                    CantidadDisponible = %s
                WHERE ProductoID = %s 
            """, (Nombre, Cantidad, ProductoID))
            mysql.connection.commit()
            
            return redirect(url_for('RegistroProductos'))

        except KeyError as e:
            return f'Error: {e}. Campo faltante en el formulario.'










if __name__ == '__main__':
    App.run(port = 3000, debug = True)



