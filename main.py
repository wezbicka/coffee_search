import json
import os
from pprint import pprint

from dotenv import load_dotenv
from geopy import distance
import folium

import fetch_coordinates


def find_distance(latitude, longitude, cafe_coords):
    length = distance.distance((latitude, longitude), cafe_coords).km
    return length


def get_distance(cafe):
    return cafe['distance']


def fetch_nearest_cafe(new_list_сoffeeshops):
    return min(new_list_сoffeeshops, key=get_distance)


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
    location = input("Где вы находитесь? ")
    coords_point = fetch_coordinates.fetch_coordinates(apikey, location)
    latitude, longitude = change_coords(coords_point)
    new_list_сoffeeshops = []
    for num, cafe in enumerate(сoffeeshops):
        cafe_coords = (
            cafe['geoData']['coordinates'][1],
            cafe['geoData']['coordinates'][0],
        )
        distance = find_distance(latitude, longitude, cafe_coords)
        new_list_сoffeeshops.append({})
        new_list_сoffeeshops[num]["title"] = cafe['Name']
        new_list_сoffeeshops[num]["distance"] = distance
        new_list_сoffeeshops[num]["latitude"] = cafe_coords[0]
        new_list_сoffeeshops[num]["longitude"] = cafe_coords[1]
        latitude, longitude = change_coords(coords_point)
    close_coffee_shops = sorted(new_list_сoffeeshops, key=get_distance)
    m = folium.Map(location=[latitude, longitude],
                   zoom_start=12,
                   tiles="Stamen Terrain")
    for cafe in sorted_list[:5]:
        folium.Marker([cafe['latitude'], cafe['longitude']],
                      popup=cafe['title'],
                      icon=folium.Icon(color="red",
                                       icon="info-sign")).add_to(m)
    m.save("index.html")


if __name__ == '__main__':
    main()
