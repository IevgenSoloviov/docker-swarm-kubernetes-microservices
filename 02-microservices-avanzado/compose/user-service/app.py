from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(service="usuaris-service", status="running")

@app.route("/usuaris/")
def usuaris():
    return jsonify([
        {
            "id": 1,
            "nom": "Ciutadà 1",
            "rol": "ciutada"
        },
        {
            "id": 2,
            "nom": "Tècnic 1",
            "rol": "tecnic"
        }
    ])

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/ready")
def ready():
    return jsonify(status="ready")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
