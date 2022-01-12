import json
import pickle
import numpy as np

__source = None
__destination = None
__airline = None
__columns = None
__model = None
__src = []
__des = []
__air = []


def get_source_names():
    return __src


def get_destination_names():
    return __des


def get_airline():
    return __air


def load_saved_artifacts():
    print("Loading saved artifacts.......start")
    global __source
    global __src
    global __des
    global __columns
    global __destination
    global __airline
    global __model
    global __air

    with open("artifacts/columns.json", "r") as f:
        __columns = json.load(f)["data_columns"]

        __airline = __columns[7:19]
        for i in range(len(__airline)):
            __air.append(__airline[i].title())

        __source = __columns[19:24]
        for i in range(len(__source)):
            __src.append((__source[i].split(sep="_")[1]).capitalize())

        __destination = __columns[24:]
        for i in range(len(__destination)):
            __des.append((__destination[i].split(sep="_")[1]).capitalize())

    with open("artifacts/model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Loading save d artifacts.....done")


def get_price(stops, journey_day, journey_month, dep_hour, dep_min, arr_hour, arr_min, airline, source, destination):
    try:
        airline_index = __columns.index(airline.lower())
        source_index = __columns.index(source.lower())
        destination_index = __columns.index(destination.lower())
    except:
        airline_index = -1
        source_index = -1
        destination_index = -1

    x = np.zeros(len(__columns))
    if airline_index >= 0:
        x[airline_index] = 1
    if source_index >= 0:
        x[source_index] = 1
    if destination_index >= 0:
        x[destination_index] = 1

    return round(__model.predict([x])[0], 2)


if __name__ == "__main__":
    load_saved_artifacts()

