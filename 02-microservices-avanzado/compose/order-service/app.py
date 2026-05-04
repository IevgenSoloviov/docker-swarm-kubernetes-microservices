from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(service="tasques-service", status="running")

@app.route("/tasques/")
def tasques():
    return jsonify([
        {
            "id": 101,
            "incidencia_id": 1,
            "tecnic": "Brigada municipal",
            "estat": "assignada"
        },
        {
            "id": 102,
            "incidencia_id": 2,
            "tecnic": "Servei de neteja",
            "estat": "en curs"
        }
    ])

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/ready")
def ready():
    return jsonify(status="ready")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
