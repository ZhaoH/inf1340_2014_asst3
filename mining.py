#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime
import math


stock_data = []
monthly_averages = []


def read_stock_data(stock_name, stock_file_name):
    """
    Read stock data and calculate stock monthly average price

    :param stock_name: The name of stock
    :param stock_file_name: The name of a JSON formatted file that contains stock data
    :return: Tuple. Consist of the average for that month, and the date (month and year)
    """

    global monthly_averages, stock_data
    monthly_averages = []
    year = None
    month = None
    volume = 0
    close_volume = 0

    stock_data = read_json_from_file(stock_file_name)

    for entry in stock_data:
        try:
            entry["Date"] = datetime.datetime.strptime(entry["Date"], '%Y-%m-%d')

            # Check if the entry is not in the same month as last entry
            if entry["Date"].month != month or entry["Date"].year != year:
                # If this is not the first entry
                if year is not None:
                    if len(str(month)) == 1:
                        month = "0" + str(month)
                    date = str(year) + "/" + str(month)
                    monthly_averages += [(date, round(close_volume/volume, 2))]

                year = entry["Date"].year
                month = entry["Date"].month
                volume = entry["Volume"]
                close_volume = entry["Close"] * entry["Volume"]

            # If this entry is in the same month as last entry
            else:
                volume += entry["Volume"]
                close_volume += entry["Close"] * entry["Volume"]

        except ValueError:
            return False

    if len(str(month)) == 1:
        month = "0" + str(month)
    date = str(year) + "/" + str(month)
    monthly_averages += [(date, round(close_volume/volume, 2))]
    return


def six_best_months():
    """
    Sort monthly stock price list and return the six months with highest stock price

    :return: A list that contains worst six months stock monthly price
    """

    # Sort list from highest price to lowest price
    best_months = sorted(monthly_averages, key=lambda bst: bst[1], reverse=True)
    if len(best_months) < 6:
        return "There is not enough data"
    else:
        return best_months[0:6]


def six_worst_months():
    """
    Sort monthly stock price list and return the six months with lowest stock price

    :return: A list that contains worst six months stock monthly price
    """

    # Sort list from lowest price to highest price
    worst_months = sorted(monthly_averages, key=lambda lst: lst[1])
    if len(worst_months) < 6:
        return "There is not enough data"
    else:
        return worst_months[0:6]


def read_json_from_file(file_name):
    """
    Read JSON file

    :param file_name: The name of a JSON formatted file that contains stock data
    :return: A list contains all the information in the JSON file
    """

    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)


def compare_two_stocks(stock_name1, stock_file_name1, stock_name2, stock_file_name2):
    """
    Compare two stocks to identify which has the highest standard deviation

    :param stock_file_name1: The name of a JSON formatted file that contains stock data
    :param stock_file_name2: The name of a JSON formatted file that contains stock data
    :return: The name of stock which has the highest standard deviation
    """

    std_deviation1 = calculate_std_deviation(stock_name1, stock_file_name1)
    std_deviation2 = calculate_std_deviation(stock_name2, stock_file_name2)

    if std_deviation1 > std_deviation2:
        return stock_name1
    elif std_deviation1 < std_deviation2:
        return stock_name2
    else:
        return "Tie"


def calculate_std_deviation(stock_name, stock_file_name):
    """
    Calculate standard deviation of monthly averages
    :param stock_name: The name of stock
    :param stock_file_name: The name of a JSON formatted file that contains stock data
    :return: float. standard deviation of the stock
    """

    total = 0
    count = 0
    total_difference = 0

    read_stock_data(stock_name, stock_file_name)

    # Calculate the average of monthly averages
    for item in monthly_averages:
        total += item[1]
        count += 1
    avg = total / count

    # Calculate the difference of each month average price from the mean, and sum the square result of each
    for item in monthly_averages:
        total_difference += math.pow(item[1] - avg, 2)

    return math.sqrt(total_difference/count)
