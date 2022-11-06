import json


def load_coffee_shops(filepath):
    with open("coffee.json", "r", encoding="CP1251") as file:
        return json.load(file)


def main():
    print(load_coffee_shops("coffee.json"))


if __name__ == '__main__':
    main()
