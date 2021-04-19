import math

LINK_STATIONS = [
    (0, 0, 10),
    (20, 20, 5),
    (10, 0, 12)
]

POINTS = [
    (0, 0),
    (100, 100),
    (15, 10),
    (18, 18)
]


def calculate_distance(x, y, station):
    x2, y2, reach = station
    return math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)


def calculate_power(reach, distance):
    return (reach - distance) ** 2 if distance <= reach else 0


def get_best_station(x, y):
    def is_best_station(_pwr):
        if best_station.get("power") is None:
            return True
        return _pwr > best_station["power"]

    best_station = {}

    for station in LINK_STATIONS:
        x2, y2, reach = station

        distance = calculate_distance(x, y, station)
        power = calculate_power(reach, distance)

        if is_best_station(power):
            best_station.update({
                "link_station": (x2, y2),
                "power": round(power, 1)
            })

    return best_station


if __name__ == '__main__':
    for point in POINTS:
        input_x, input_y = point
        station_details = get_best_station(input_x, input_y)

        if station_details["power"] == 0:
            print(f"No link station within reach for point {input_x}, {input_y}")
            continue

        station_x, station_y = station_details["link_station"]
        pwr = station_details["power"]
        print(f"Best link station for point {input_x}, {input_y} is {station_x}, {station_y} with power {pwr}")

