from flask import Flask, jsonify, request
import json
from datetime import datetime

app = Flask(__name__)

# Función para cargar los datos de un archivo JSON
def cargar_json(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

# Carga de datos
precipitaciones = cargar_json("precipitaciones.json")
temperaturas = cargar_json("temperatura.json")
vientos = cargar_json("viento.json")

# Función para filtrar por fecha
def filtrar_por_fecha(datos, fecha_str):
    resultados = []
    for item in datos:
        if item["date"].startswith(fecha_str):
            resultados.append(item)
    return resultados

@app.route("/weather")
def weather():
    fecha = request.args.get("date")
    if not fecha:
        return jsonify({"error": "Falta parámetro 'date'"}), 400
    
    # Extraemos solo la parte de la fecha (YYYY-MM-DD)
    fecha_simple = fecha[:10]

    # Filtramos cada JSON
    resultado = {
        "precipitaciones": filtrar_por_fecha(precipitaciones, fecha_simple),
        "temperaturas": filtrar_por_fecha(temperaturas, fecha_simple),
        "vientos": filtrar_por_fecha(vientos, fecha_simple)
    }

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)
