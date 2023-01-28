import json
import sys


def main():
    titles_by_category = {}

    with open("output.json", "r") as data:
        json_data = json.load(data)
        for item in json_data:
            if item["category"] not in titles_by_category:
                titles_by_category[item["category"]] = item["title_and_price"]
            else:
                titles_by_category[item["category"]].update(item["title_and_price"])

    print(titles_by_category)


if __name__ == "__main__":
    main()
