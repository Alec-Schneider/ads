"""
functions for working with fangraphs datasets

"""

import numpy as np
import pandas as pd
from functools import reduce


def clean_pcts(x):
    """"
    Intended to be used be used in the .apply() method of 
    """
    if type(x) in (int, float):
        return float(x)
    else:
        return float(x.replace('%', '').strip()) / 100

