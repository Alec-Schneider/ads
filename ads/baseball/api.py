"""
functions for working with fangraphs datasets

"""
import pandas as pd


def clean_pcts(x):
    """"
    Intended to be used be used in the .apply() method of 
    """
    if type(x) in (int, float):
        return float(x)
    else:
        return float(x.replace('%', '').strip()) / 100

