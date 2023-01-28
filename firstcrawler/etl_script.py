import json
import sys


def main():
    with open("output.json", "r") as data:

        json_data = data.map(lambda dictionary: json.loads(dictionary))
        for item in json_data:
            print(item.category)


if __name__ == "__main__":
    main()
