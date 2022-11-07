import json


def load_coffee_shops(filepath):
    with open("coffee.json", "r", encoding="CP1251") as file:
        return json.load(file)


def main():
    сoffeeshops = load_coffee_shops("coffee.json")
    for num, cafe in enumerate(сoffeeshops):
        cafe_coords = (cafe['geoData']['coordinates'][1],
                       cafe['geoData']['coordinates'][0])
        cafe_name = cafe['Name']

    print(cafe_name, cafe_coords)


if __name__ == '__main__':
    main()
