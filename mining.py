#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"


"""
    1. Read json file
    2. Required fields: date, volume, close price
    3. How many data points are there in the JSON file for that month (import datetime - Sasa used it)
    4. Calculate monthly average
    5. In tuple - put calculated monthly average with the month and year
    6. Append tuple to a list - monthly_averages_list
"""

# imports one per line
import json
import datetime





REQUIRED_FIELDS = ["Date", "Close", "Volume"]

stock_data = []
monthly_averages = []


def read_stock_data(stock_name, stock_file_name):
    """
    Read stock data and calculate stock monthly average price
    :param stock_name: The name of stock
    :param stock_file_name: The name of a JSON formatted file that contains stock data
    :return: Tuple. Consist of the average for that month, and the date (month and year)
    """

    with open(stock_file_name) as file_handle:
        file_contents = file_handle.read()
        json.loads(file_contents)






    return



def average_per_month(date_string):
    """
    Identifies the month and year from format YYYY-MM-DD
    :param date_string: date to be checked
    :return: tuple with monthly average, month, and year
    """

#    try:
#        datetime.datetime.strptime(date_string, '%Y-%m-%d')
#        return True



def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]




