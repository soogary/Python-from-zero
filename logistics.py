from geopy import distance

# build a list of US cities 
CITIES = [
    ("New York City", 40.7128, -74.0060),
    ("Los Angeles", 34.0522, -118.2437),
    ("Chicago", 41.8781, -87.6298),
    ("Houston", 29.7604, -95.3698),
    ("Philadelphia", 39.9526, -75.1652),
    ("Phoenix", 33.4484, -112.0740),
    ("San Antonio", 29.4241, -98.4936),
    ("San Diego", 32.7157, -117.1611),
    ("Dallas", 32.7767, -96.7970),
    ("San Jose", 37.3382, -121.8863),
]

def distance_between(point1, point2):
    
    return distance.distance(point1, point2).miles


def find_coodinates(city):
    for city_name, coordinates in CITIES:
        if city_name == city:
            return coordinates
    return city.latitude, city.longitude


def distance_miles(cities):
    """calculate distance between 2 cities in miles"""
    total = 0
    for i in range(len(cities) - 1):
        total += distance_between(cities[i], cities[i+1])
    return total

def print_cities():

    for city in CITIES:
        print(city[0])
    return[city[0] for city in CITIES]


def travel_time(city1, city2, speed=60):
    """default speed 60mph"""
    return distance_between(find_coodinates(city1), find_coodinates(city2)) / speed

#print(distance_between(CITIES[0][1], CITIES[1][1]))
print_cities()

#if __name__ == '__main__':
  