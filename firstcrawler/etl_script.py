import json
import pandas as pd
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

    # alert if any category has a different number of titles than is expected
    for entry in titles_by_category:
        expected_total = int(titles_by_category[entry][0])
        actual_total = len(titles_by_category[entry][1])

        if expected_total != actual_total:
            print(
                entry
                + ": "
                + titles_by_category[entry][0]
                + " vs "
                + str(len(titles_by_category[entry][1]))
                + "\n\n"
                + str(titles_by_category[entry][1])
            )

    index = ["category", "total price", "average price"]
    df = pd.DataFrame(columns=index)

    # iterate through and show the total of all book prices in a category, and the average cost of a book in that category
    for category in titles_by_category:
        total = 0.00
        for title in titles_by_category[category][1]:
            with_currency_symbol = titles_by_category[category][1][title]
            amount = float(with_currency_symbol[1::])
            total += amount

        average_price = total / int(titles_by_category[category][0])

        print(
            f"Category: {category} => Total: {round(total, 2)} => Avg Price: {round(average_price, 2)}"
        )

        temp_series = pd.Series(
            [category, round(total, 2), round(average_price, 2)], index=index
        )
        df = pd.concat([df, temp_series.to_frame().T], ignore_index=True)

        df.to_csv("output.csv", index=False)


if __name__ == "__main__":
    main()
