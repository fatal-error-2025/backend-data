from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Función para cargar un JSON si existe
def load_json(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Cargar datos de los tres JSON
temperatura = load_json("sample.json")
tiempo = load_json("sample.json")
precipitaciones = load_json("sample.json")

@app.route("/")
def index():
    return "Backend funcionando ✅"

@app.route("/weather")
def weather():
    date = request.args.get("date")
    if not date:
        return jsonify({"error": "Falta parámetro 'date'"}), 400

    # Filtrar cada dataset por la fecha exacta
    temp_result = [t for t in temperatura if t.get("date") == date]
    tiempo_result = [t for t in tiempo if t.get("date") == date]
    precip_result = [p for p in precipitaciones if p.get("date") == date]

    # Si no hay ningún resultado en ninguna categoría
    if not (temp_result or tiempo_result or precip_result):
        return jsonify({"error": "No se encontraron datos para esa fecha"}), 404

    # Devolver todo junto
    return jsonify({
        "fecha": date,
        "temperatura": temp_result,
        "tiempo": tiempo_result,
        "precipitaciones": precip_result
    })

if __name__ == "__main__":
    app.run(debug=True)
