from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Cargar JSON de precipitaciones
with open("sample.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ruta de prueba
@app.route("/")
def index():
    return "Backend funcionando ✅"

# Ruta para obtener precipitaciones por fecha
@app.route("/precipitaciones")
def precipitaciones():
    date = request.args.get("date")
    if not date:
        return jsonify({"error": "Falta parámetro 'date'"}), 400
    
    # Filtrar los datos por fecha
    result = [p for p in data if p.get("date") == date]
    
    if not result:
        return jsonify({"error": "No se encontraron datos para esa fecha"}), 404
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
