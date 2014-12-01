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

    return


def six_best_months():
    """
    Sort monthly stock price list and return the six months with highest stock price

    :return: A list that contains worst six months stock monthly price
    """

    # Sort list from highest price to lowest price
    best_months = sorted(monthly_averages, key=lambda bst: bst[1], reverse=True)

    return best_months[0:6]


def six_worst_months():
    """
    Sort monthly stock price list and return the six months with lowest stock price

    :return: A list that contains worst six months stock monthly price
    """

    # Sort list from lowest price to highest price
    worst_months = sorted(monthly_averages, key=lambda lst: lst[1])

    return worst_months[0:6]


def read_json_from_file(file_name):
    """
    Read Jason file

    :param file_name: Jason file
    :return: A list contains all the information in the Jason file
    """

    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)
