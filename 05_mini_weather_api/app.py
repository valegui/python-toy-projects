from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    "New York": {"temperature": 20, "condition": "Sunny", "icon": "sunny"},
    "London": {
        "temperature": 18,
        "condition": "Cloudy",
        "icon": "cloudy",
    },
    "Paris": {
        "temperature": 22,
        "condition": "Rainy",
        "icon": "rainy",
    },
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


if __name__ == "__main__":
    app.run(debug=True)
