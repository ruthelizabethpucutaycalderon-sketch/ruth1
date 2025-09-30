from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return "<h1>Bienvenido a mi app Flask</h1><p>Hola mundo desde Flask</p>"

# Ruta con parámetros y métodos POST/GET
@app.route('/saludo', methods=['GET', 'POST'])
def saludo():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        return f"<h2>¡Hola, {nombre}!</h2>"
    return '''
        <form method="POST">
            <label>Nombre: <input type="text" name="nombre"></label>
            <input type="submit" value="Saludar">
        </form>
    '''

# Ruta con parámetro en la URL
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f"<h3>Perfil del usuario: {nombre}</h3>"

# Ruta de redirección
@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('home'))

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)
