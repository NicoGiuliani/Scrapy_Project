import json
import random
import sys


def main():
    titles_by_category = {}

    with open("output.json", "r") as data:
        json_data = json.load(data)
        for obj in json_data:
            current_titles = obj["titles"]
            current_prices = obj["prices"]

            if obj["valid"] == False:
                print("alert: possible missing entries")
            else:
                prices_by_title = {}
                current_category = obj["category"]
                number_of_titles = obj["number_results"]

                for i in range(len(current_titles)):
                    current_title = current_titles[i]
                    current_price = current_prices[i]

                    if current_title not in prices_by_title:
                        prices_by_title[current_title] = current_price
                    else:
                        # if the title is already in the dict, append a suffix to it
                        suffix = str(random.randrange(10000, 99999))
                        prices_by_title[current_title + "_" + suffix] = current_price

                if current_category not in titles_by_category:
                    titles_by_category[current_category] = (
                        number_of_titles,
                        prices_by_title,
                    )
                else:
                    # if the category already exists:
                    for title in prices_by_title:
                        if title not in titles_by_category[current_category][1]:
                            titles_by_category[current_category][1][
                                title
                            ] = prices_by_title[title]
                        # else:
                        #     suffix = str(random.randrange(10000, 99999))
                        #     titles_by_category[current_category][1][
                        #         title + "_" + suffix
                        #     ] = prices_by_title[title]

    for entry in titles_by_category:
        print(
            entry
            + ": "
            + titles_by_category[entry][0]
            + " vs "
            + str(len(titles_by_category[entry][1]))
        )


if __name__ == "__main__":
    main()
