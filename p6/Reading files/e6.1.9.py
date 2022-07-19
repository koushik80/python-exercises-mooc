# E-6.1.9: City bikes

# Problem: https://programming-22.mooc.fi/part-6/1-reading-files#programming-exercise-city-bikes


# Sample output:


# Solution:

import math


def get_station_data(filename: str):

    station_record = {}

    with open(filename) as station_data:
        for line in station_data:
            line = line.replace('\n', '')
            parts = line.split(';')
            if parts[0] == "Longitude":
                continue
            station_record[parts[3]] = float(parts[0]), float(parts[1])

    return station_record


def distance(stations: dict, station1: str, station2: str):

    for station, coordinates in stations.items():
        if station1 in station:
            x = coordinates
        if station2 in station:
            y = coordinates
    x_km = (x[0] - y[0]) * 55.26
    y_km = (x[1] - y[1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km


def greatest_distance(stations: dict):

    bol = True

    for station_name, info in stations.items():
        station1 = station_name
        longitude1 = info[0]
        latitude1 = info[1]

        for another_station_name, another_station_info in stations.items():
            station2 = another_station_name
            longitude2 = another_station_info[0]
            latitude2 = another_station_info[1]
            x_km = (longitude1 - longitude2) * 55.26
            y_km = (latitude1 - latitude2) * 111.2
            distance_km = math.sqrt(x_km**2 + y_km**2)

            if bol or distance_km > remote:
                remote = distance_km
                station1_name = station1
                station2_name = station2
                bol = False

    return station1_name, station2_name, remote


if __name__ == '__main__':
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
