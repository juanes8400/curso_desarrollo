from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)


def get_db_connection():
  conn = sqlite3.connect('censo.db')  # conectar a la base de datos
  conn.row_factory = sqlite3.Row
  return conn


#Ruta para la página de inicio


@app.route('/')
def index():
  return render_template_string(''' 
  <h1> Busqueda en el Censo </h1>
  <form action="/buscar" method="post">
    <label for="tipo">Busca por:</label>
    <select name="tipo" id="tipo">
      <option value="numero">Numero</option>
      <option value="nombre">Nombre</option>
    </select>
    <label for="valor">Valor:</label>
    <input type="text" name="valor" id="valor" required>
    <button type="submit">Buscar</Button>
  </form>
  ''')


#Ruta para realizar la busqueda
@app.route('/buscar', methods=['POST'])
def buscar():
  tipo = request.form['tipo']
  valor = request.form['valor']
  conn = get_db_connection()
  registro = None

  if tipo == 'numero':
    registro = conn.execute('SELECT * FROM censo Where numero = ?',
                            (valor, )).fetchone()
  elif tipo == 'nombre':
    registro = conn.execute('SELECT * FROM censo WHERE nombre = ?',
                            (valor, )).fetchone()

  conn.close()

  if registro:
    return render_template_string('''
    <p>Número: {{ registro['numero'] }}</p>
    <p>Nombre: {{ registro['nombre'] }}</p>
    <p>Edad: {{ registro['edad'] }}</p>
    <p>Impuestos: {{ registro['impuestos'] }}</p>
    <a href="/">Volver</a>
    ''',
                                  registro=registro)
  else:
    return 'Registro no encontrado. <a href="/">Volver</a>'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)
