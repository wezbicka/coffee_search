import json


def main():
    with open("coffee.json", "r", encoding="CP1251") as file:
        file_content = json.load(file)
        print(file_content)


if __name__ == '__main__':
    main()
