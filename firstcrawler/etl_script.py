import json
import random
import sys


def main():
    titles_by_category = {}

    with open("output.json", "r") as data:
        json_data = json.load(data)
        for obj in json_data:
            # two variables below represent the titles & prices on a single page
            current_titles = obj["titles"]
            current_prices = obj["prices"]

            if obj["valid"] == False:
                print("alert: possible missing entries")
            else:
                prices_by_title = {}
                current_category = obj["category"]
                number_of_titles = obj["number_results"]

                # iterate through all products on a page, adding them to the price_by_title dictionary
                for i in range(len(current_titles)):
                    # two variables belwo represent the title & price of a single product
                    current_title = current_titles[i]
                    current_price = current_prices[i]

                    if current_title not in prices_by_title:
                        prices_by_title[current_title] = current_price
                    else:
                        suffix = str(i)
                        prices_by_title[current_title + "_" + suffix] = current_price

                # add new or update existing category with data from the current page
                if current_category not in titles_by_category:
                    titles_by_category[current_category] = (
                        number_of_titles,
                        prices_by_title,
                    )
                else:
                    titles_in_current_category = titles_by_category[current_category][1]
                    for title in prices_by_title:
                        if title not in titles_in_current_category:
                            titles_in_current_category[title] = prices_by_title[title]

    for entry in titles_by_category:
        if int(titles_by_category[entry][0]) != len(titles_by_category[entry][1]):
            print(
                entry
                + ": "
                + titles_by_category[entry][0]
                + " vs "
                + str(len(titles_by_category[entry][1]))
                + "\n\n"
                + str(titles_by_category[entry][1])
            )


if __name__ == "__main__":
    main()
