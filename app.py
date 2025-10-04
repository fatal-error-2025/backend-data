from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])  # 👈 habilitar CORS para todas las rutas

# Cargar JSON de precipitaciones
with open("sample.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@app.route("/")
def index():
    return "Backend funcionando ✅"

@app.route("/precipitaciones")
def precipitaciones():
    date = request.args.get("date")
    if not date:
        return jsonify({"error": "Falta parámetro 'date'"}), 400

    result = [p for p in data if p.get("date") == date]

    if not result:
        return jsonify({"error": "No se encontraron datos para esa fecha"}), 404

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
