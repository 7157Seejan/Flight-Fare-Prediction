from flask import Flask, request, jsonify
import util
import pandas as pd

app = Flask(__name__)


@app.route("/get_source_names")
def get_source_names():
    response = jsonify({
        "source": util.get_source_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/get_destination_names")
def get_destination_names():
    response = jsonify({
        "destination": util.get_destination_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/get_airline")
def get_airline():
    response = jsonify({
        "airline": util.get_airline()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/predict_price", methods=["POST"])
def predict_price():
    # Date_of_Journey
    journey_date = request.form["journey_date"]
    journey_day = int(pd.to_datetime(journey_date, format="%Y-%m-%d").day)
    journey_month = int(pd.to_datetime(journey_date, format="%Y-%m-%d").month)

    # Departure
    dep_time = request.form["departure_time"]
    dep_hour = int(pd.to_datetime(dep_time, format="%H:%M").hour)
    dep_min = int(pd.to_datetime(dep_time, format="%H:%M").minute)

    # Arrival
    arr_time = request.form["arrival_time"]
    arr_hour = int(pd.to_datetime(arr_time, format="%H:%M").hour)
    arr_min = int(pd.to_datetime(arr_time, format="%H:%M").minute)

    # Total Stops
    stops = int(request.form["stops"])

    # Airline
    airline = request.form['airline']

    # Source
    source = "source_" + request.form["source"]

    # Destination
    destination = "destination_" + request.form["destination"]

    response = jsonify({
        'estimated_fare': util.get_price(stops, journey_day, journey_month, dep_hour, dep_min, arr_hour, arr_min, airline, source, destination)
    })

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    print("Starting server...")
    util.load_saved_artifacts()
    app.run()
