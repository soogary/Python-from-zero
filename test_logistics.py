#from logistics import CITIES, distance_between, print_cities
from logistics import CITIES, print_cities

#def test_distance_between():
#    assert distance_between(CITIES[0][1], CITIES[1][1])

def test_print_cities():
    assert "Dallas" in print_cities()
