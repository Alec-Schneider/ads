"""
Uses pandas and fredapi (Federal Reserve api made to retrieve data Pandas Series) and
pulls in the entire series of any data you would like to retrieve.
"""

from fredapi import Fred


def fetch_fred(name, api_key):
    """
    parameters
    ------------
    name: str; required
        FRED series name to fetch

    return
    ------------
        pandas Series of FRED data
    """
    fred = Fred(api_key)
    data = fred.get_series(name)
    return data


