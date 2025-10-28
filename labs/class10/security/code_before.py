import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, password TEXT)")
    cur.execute("INSERT INTO users VALUES (1,'admin','secret')")
    conn.commit()
    return conn

@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("name", "")
    password = request.form.get("password", "")
    # VULNERABLE: SQL concatenation allows injection like: ' OR 1=1 --
    query = f"SELECT id,name FROM users WHERE name = '{name}' AND password = '{password}'"
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute(query)  # <-- vulnerable call
        row = cur.fetchone()
        if row:
            return jsonify({"ok": True, "user": row[1]})
        return jsonify({"ok": False}), 401
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)
