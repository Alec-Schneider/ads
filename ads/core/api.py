import numpy as np
import pandas as pd
from functools import reduce
from itertools import chain


def get_data(file_path, **kwargs):
    """
    parameters
    ------------
    file_path: str, required.
        path to .csv or .xlsx file to read
    kwargs
    chunksize:
        amount of rows to read

    return
    ------------
    iostream of DataFrames
    """
    assert (file_type in ('csv', 'txt', 'xlsx', 'ftr')), \
            'Only .xslx, .csv, .txt, and .ftr files can be passed to function'

    # creating data as None incase neither of conditions are
    file_type = file_path.split('.')[-1]
    if file_type in ['csv', 'txt']:
        data = pd.read_csv(file_path, **kwargs)
    elif file_type in ['xlsx']:
        data = pd.read_excel(file_path, **kwargs)
    elif file_type in ['ftr']:
        data = pd.read_feather(file_path, **kwargs)
    else:
    return data


def merge_files(paths, on, how='inner', drop_dup_cols=True, **kwargs):
    """
    parameters
    ------------
    paths: list, tuple; required.
        path to .csv or .xlsx file to read
    on: str, list, or tuple; required
        columns to merge the data on
    how: str; required; inner is default, but options are also left, right, and outer
        type of merge to conduct

    return
    ------------
    merged DataFrame of all files
    """

    # chains = [get_data(p,**kwargs) for p in paths]
    # if 'chunksize' in kwargs.keys():
    #     dfs = chain(*chains)
    #
    # else:
    dfs = chain([get_data(p, **kwargs) for p in paths])

    right = '_right'
    merged_data = reduce(lambda x, y: pd.merge(x, y, on=on, how=how, suffixes=('', right)), dfs)
    if drop_dup_cols:
        merged_data.drop([col for col in merged_data.columns if right in col], axis=1, inplace=True)

    return merged_data