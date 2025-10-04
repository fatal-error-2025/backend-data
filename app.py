from flask import Flask, jsonify, request
import json
import os
from flask_cors import CORS  # <-- Importamos CORS

app = Flask(__name__)
CORS(app)  # <-- Habilitamos CORS solo para este origen

# Carpeta donde están los JSON
DATA_DIR = "data"

# Función para cargar los datos de un archivo JSON
def cargar_json(nombre_archivo):
    ruta = os.path.join(DATA_DIR, nombre_archivo)
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

# Carga de datos
precipitaciones = cargar_json("precipitaciones.json")
temperaturas = cargar_json("temperatura.json")
humedades = cargar_json("tiempo.json")

# Función para filtrar por fecha (YYYY-MM-DD)
def filtrar_por_fecha(datos, fecha_str):
    return [item for item in datos if item["date"].startswith(fecha_str)]

# Ruta de prueba para ver que la API funciona
@app.route("/")
def home():
    return jsonify({"message": "API de clima funcionando. Usa /weather?date=YYYY-MM-DD"}), 200

# Ruta principal para obtener el clima por fecha
@app.route("/weather")
def weather():
    fecha = request.args.get("date")
    if not fecha:
        return jsonify({"error": "Falta parámetro 'date'"}), 400
    
    fecha_simple = fecha[:10]
    
    resultado = {
        "precipitaciones": filtrar_por_fecha(precipitaciones, fecha_simple),
        "temperaturas": filtrar_por_fecha(temperaturas, fecha_simple),
        "humedades": filtrar_por_fecha(humedades, fecha_simple)
    }

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)
