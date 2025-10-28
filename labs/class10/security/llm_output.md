import sqlite3
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, password TEXT)")
    cur.execute("INSERT INTO users VALUES (1,'admin','secret')")
    conn.commit()
    return conn

def validate_input(input_string, max_length=50):
    """
    Validación básica de entradas para prevenir caracteres maliciosos.
    - Verifica longitud máxima
    - Solo permite caracteres alfanuméricos, guiones bajos y guiones medios
    """
    if not input_string or len(input_string) > max_length:
        return False
    # Solo permite letras, números, guiones bajos y guiones medios
    if not re.match(r'^[a-zA-Z0-9_-]+$', input_string):
        return False
    return True

@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("name", "")
    password = request.form.get("password", "")
    
    # SEGURIDAD: Validación de entradas antes de procesar
    if not validate_input(name) or not validate_input(password):
        return jsonify({"ok": False, "error": "Invalid input format"}), 400
    
    # SEGURIDAD: Uso de consultas parametrizadas (prepared statements)
    # Los placeholders '?' previenen la inyección SQL porque los valores
    # se tratan como datos, no como parte de la consulta SQL
    query = "SELECT id, name FROM users WHERE name = ? AND password = ?"
    
    conn = get_db()
    cur = conn.cursor()
    try:
        # Los parámetros se pasan como tupla separada de la consulta
        # Esto asegura que los valores no se interpreten como código SQL
        cur.execute(query, (name, password))
        row = cur.fetchone()
        
        if row:
            return jsonify({"ok": True, "user": row[1]})
        
        # No revelar si el usuario existe o la contraseña es incorrecta
        return jsonify({"ok": False, "error": "Invalid credentials"}), 401
    
    except sqlite3.Error as e:
        # Manejo de errores sin exponer detalles internos
        return jsonify({"ok": False, "error": "Database error"}), 500
    
    finally:
        conn.close()

if __name__ == "__main__":
    # NOTA: En producción, usar debug=False
    app.run(debug=True)

Principales mejoras de seguridad:
Consultas parametrizadas: Uso de ? como placeholders y pasar valores como tupla separada
Validación de entradas: Función que verifica formato y longitud de los datos
Manejo de errores: No expone información sensible sobre la base de datos
Mensajes genéricos: No revela si falló el usuario o la contraseña
Diferencia clave: Antes f"...'{name}'..." permitía inyección. Ahora "... WHERE name = ?" con (name,) separa datos de código SQL.