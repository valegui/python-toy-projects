from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    "New York": {"temperature": 20, "condition": "Sunny"},
    "London": {"temperature": 18, "condition": "Cloudy"},
    "Paris": {"temperature": 16, "condition": "Rainy"},
    "Tokyo": {"temperature": 24, "condition": "Sunny"},
    "Sydney": {"temperature": 28, "condition": "Sunny"},
    "Mumbai": {"temperature": 26, "condition": "Sunny"},
    "Beijing": {"temperature": 22, "condition": "Sunny"},
    "Seoul": {"temperature": 20, "condition": "Clear"},
}


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Weather API"})


@app.route("/weather", methods=["GET"])
def weather():
    return jsonify(weather_data)


@app.route("/weather/<city>", methods=["GET"])
def weather_by_city(city):
    city = city.capitalize()
    if city in weather_data:
        return jsonify({city: weather_data[city]})
    return jsonify({"error": "City not found"}), 404


@app.route("/weather", methods=["POST"])
def add_weather():
    data = request.get_json()
    city = data.get("city", "").capitalize()
    temperature = data.get("temperature")
    condition = data.get("condition")
    if city and temperature and condition:
        weather_data[city] = {"temperature": temperature, "condition": condition}
        return jsonify({"message": f"Weather data for {city} added successfully"}), 201
    return jsonify({"error": "Invalid data"}), 400


@app.route("/weather/<city>", methods=["PUT"])
def update_weather(city):
    city = city.capitalize()
    data = request.get_json()
    temperature = data.get("temperature")
    condition = data.get("condition")
    if city and temperature and condition:
        weather_data[city] = {"temperature": temperature, "condition": condition}
        return jsonify(
            {"message": f"Weather data for {city} updated successfully"}
        ), 200
    return jsonify({"error": "Invalid data"}), 400


@app.route("/weather/<city>", methods=["DELETE"])
def delete_weather(city):
    city = city.capitalize()
    if city in weather_data:
        del weather_data[city]
        return jsonify(
            {"message": f"Weather data for {city} deleted successfully"}
        ), 200
    return jsonify({"error": "City not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
