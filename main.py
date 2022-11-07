import json
import os

from dotenv import load_dotenv
from geopy import distance

import fetch_coordinates


def find_distance(latitude, longitude, cafe_coords):
    length = distance.distance((latitude, longitude), cafe_coords).km
    return length


def load_coffee_shops(filepath):
    with open("coffee.json", "r", encoding="CP1251") as file:
        return json.load(file)


def change_coords(coords_user_point):
    longitude, latitude = coords_user_point
    return latitude, longitude


def main():
    load_dotenv()
    apikey = os.environ['apikey']
    сoffeeshops = load_coffee_shops("coffee.json")
    for num, cafe in enumerate(сoffeeshops):
        cafe_coords = (cafe['geoData']['coordinates'][1],
                       cafe['geoData']['coordinates'][0])
        cafe_name = cafe['Name']

    print(cafe_name, cafe_coords)

    location = input("Где вы находитесь? ")
    coords_point = fetch_coordinates.fetch_coordinates(apikey, location)
    latitude, longitude = change_coords(coords_point)
    distance = find_distance(latitude, longitude, cafe_coords)
    print(distance)


if __name__ == '__main__':
    main()
