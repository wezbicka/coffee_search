import json


def load_coffee_shops(filepath):
    with open("coffee.json", "r", encoding="CP1251") as file:
        return json.load(file)


def main():
    file_content = load_coffee_shops("coffee.json")
    cafe_name = file_content[0]['Name']
    print(cafe_name)


if __name__ == '__main__':
    main()
