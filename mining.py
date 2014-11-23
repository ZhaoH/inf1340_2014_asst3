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

#import json

stock_data = []
monthly_averages = []


def read_stock_data(stock_name, stock_file_name):
    """
    Read stock data and calculate stock monthly average price
    :param stock_name: The name of stock
    :param stock_file_name: The name of a JSON formatted file that contains stock data
    :return: Tuple. Consist of the average for that month, and the date (month and year)
    """
    return

#REQUIRED_FIELDS = ["date", "close", "volume"]
#average price = (V1  C1 + V2  C2)=(V1 + V2)
#monthly_averages_list: tuple of averages for each month

#from last assignment:
#def valid_date_format(date_string):
#    """
#    Checks whether a date has the format YYYY-mm-dd in numbers
#    :param date_string: date to be checked
#   :return: Boolean True if the format is valid, False otherwise
#    """
#    try:
#        datetime.datetime.strptime(date_string, '%Y-%m-%d')
#        return True



def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)

