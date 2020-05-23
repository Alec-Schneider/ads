import pandas as pd
from itertools import chain
import multiprocessing as mp
from ads.core.api import get_data

def stream_sums(chunks):
    """
    
    """
    sums = pd.Series(dtype='float')
    nrows = 0
    nulls = 0

    for chunk in chunks:
        nulls += chunk.isnull().sum()
        if sums.empty:
            sums = chunk.sum(numeric_only=True)
        else:
            sums += chunk.sum(numeric_only=True)
        nrows += chunk.shape[0] - chunk[sums.index].isnull().sum()

    return sums, nrows

def stream_avg(chunks):
    """
    path: str; required
        path to file
    chunksize:
        chunk
    """
    sums, nrows = stream_sums(chunks)
    means = sums / nrows

    return means


def stream_aggs(paths, agg, chunksize=250, pool=None, **kwargs):
    """
    Credit to Max Halford (https://github.com/MaxHalford for this function)
    would import his function, but I don't believe he added it to his xam
    toolkit, and would not like his personal toolkit to be a dependency for
    this package.

    paths:
        file path
    key:
        key to groupby
    agg:
        function passed to return aggregate results
    chunksize:
        amount of rows to read into each chunk of data

    """
    if not isinstance(paths, list):
        paths = [paths]

    kwargs['chunksize'] = chunksize
    chunks = chain(*[get_data(p, **kwargs) for p in paths])
    results = []
    for chunk in chunks:
        if pool:
            results.append(pool.apply_async(agg, args=(chunk,)))
        else:
            results.append(agg(chunk))

    if pool:
        results = [r.get() for r in results]

    return pd.concat(results)




