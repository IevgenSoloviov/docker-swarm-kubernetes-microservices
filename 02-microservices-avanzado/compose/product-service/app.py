from flask import Flask, jsonify, request
import pymysql
import os
import time

app = Flask(__name__)
start_time = time.time()
VERSION = "v3-db"

DB_HOST = os.getenv("DB_HOST", "db-products")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD", "root")
DB_NAME = os.getenv("PRODUCTS_DB", "incidencies_db")


def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )


def init_db():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS incidencies (
                id INT AUTO_INCREMENT PRIMARY KEY,
                tipus VARCHAR(100) NOT NULL,
                descripcio VARCHAR(255) NOT NULL,
                ubicacio VARCHAR(150) NOT NULL,
                estat VARCHAR(50) DEFAULT 'pendent'
            )
        """)

        cur.execute("SELECT COUNT(*) AS total FROM incidencies")
        total = cur.fetchone()["total"]

        if total == 0:
            cur.executemany("""
                INSERT INTO incidencies (tipus, descripcio, ubicacio, estat)
                VALUES (%s, %s, %s, %s)
            """, [
                ("Enllumenat", "Farola apagada al Passeig de Mar", "Passeig de Mar", "pendent"),
                ("Neteja viària", "Acumulació de residus a la via pública", "Carrer Ample", "en procés"),
                ("Mobiliari urbà", "Banc deteriorat a la plaça", "Plaça Catalunya", "resolta")
            ])

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return jsonify(
        service="incidencies-service",
        version=VERSION,
        status="running",
        database="mysql"
    )


@app.route("/incidencies/", methods=["GET"])
def get_incidencies():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM incidencies ORDER BY id")
        data = cur.fetchall()
    conn.close()
    return jsonify(data)


@app.route("/incidencies/", methods=["POST"])
def crear_incidencia():
    data = request.get_json()

    tipus = data.get("tipus")
    descripcio = data.get("descripcio")
    ubicacio = data.get("ubicacio")

    if not tipus or not descripcio or not ubicacio:
        return jsonify(error="Falten camps obligatoris"), 400

    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO incidencies (tipus, descripcio, ubicacio, estat)
            VALUES (%s, %s, %s, %s)
        """, (tipus, descripcio, ubicacio, "pendent"))
        new_id = cur.lastrowid

    conn.commit()
    conn.close()

    return jsonify(
        id=new_id,
        tipus=tipus,
        descripcio=descripcio,
        ubicacio=ubicacio,
        estat="pendent"
    ), 201


@app.route("/incidencies/<int:incidencia_id>", methods=["DELETE"])
def eliminar_incidencia(incidencia_id):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM incidencies WHERE id = %s", (incidencia_id,))
    conn.commit()

    eliminada = cursor.rowcount

    cursor.close()
    conn.close()

    if eliminada == 0:
        return jsonify(error="Incidència no trobada"), 404

    return jsonify(
        message="Incidència eliminada correctament",
        id=incidencia_id
    )


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/ready")
def ready():
    return jsonify(status="ready")


@app.route("/metrics")
def metrics():
    uptime = time.time() - start_time
    return f"""
# HELP incidencies_service_uptime_seconds Uptime
# TYPE incidencies_service_uptime_seconds counter
incidencies_service_uptime_seconds {uptime}
"""


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
