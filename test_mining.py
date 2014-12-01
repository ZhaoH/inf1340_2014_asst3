#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
from mining import *


def test_goog():
    read_stock_data("GOOG", "data/GOOG.json")
    assert six_best_months() == [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38), ('2008/1', 599.42),
                                 ('2008/5', 576.29), ('2008/6', 555.34)]
    assert six_worst_months() == [('2004/9', 116.38), ('2004/10', 164.52), ('2004/11', 177.09), ('2004/12', 181.01),
                                  ('2005/3', 181.18), ('2005/1', 192.96)]


def test_tseso():
    read_stock_data("TSE-SO", "data/TSE-SO.json")
    assert six_best_months() == [('2007/12', 20.98), ('2007/11', 20.89), ('2013/5', 19.96), ('2013/4', 19.65),
                                 ('2007/10', 19.11), ('2008/2', 18.93)]
    assert six_worst_months() == [('2009/3', 1.74), ('2008/11', 2.08), ('2008/12', 2.25), ('2009/2', 2.41),
                                  ('2009/4', 2.75), ('2009/1', 3.14)]


test_goog()
test_tseso()