from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/weather", methods=["GET"])
def get_weather():
    date = request.args.get("date")
    if not date:
        return jsonify({"error": "date parameter is required"}), 400

    response = {}
    for category in ["temperatura", "tiempo", "precipitaciones"]:
        file_path = os.path.join(BASE_DIR, category, "sample.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Buscar registros que coincidan con la fecha
            filtered = [entry for entry in data if entry["date"].startswith(date)]
            response[category] = filtered

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
