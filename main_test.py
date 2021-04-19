from main import get_best_station, calculate_distance, calculate_power


def test_get_best_station_positive():
    val = get_best_station(0, 0)
    assert val["power"] == 100
    assert val["link_station"] == (0, 0)


def test_get_best_station_positive2():
    val = get_best_station(5, 5)
    assert val["power"] == 24.3
    assert val["link_station"] == (10, 0)


def test_get_best_station_no_station():
    val = get_best_station(100, 100)
    assert val["power"] == 0


def test_calculate_power():
    val = calculate_power(10, 9)
    assert val == 1


def test_calculate_power_zero():
    val = calculate_power(10, 11)
    assert val == 0


def test_calculate_distance():
    val = calculate_distance(0, 0, (0, 0, 10))
    assert val == 0


def test_calculate_distance2():
    val = calculate_distance(10, 0, (0, 0, 10))
    assert val == 10


def test_calculate_distance3():
    val = calculate_distance(10, 10, (0, 0, 10))
    assert val == 14.142135623730951
