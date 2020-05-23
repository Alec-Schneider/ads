import pandas as pd
from scipy.stats import pearsonr
import numpy as np


def get_pearsonr(X, y):
    """
    parameters
    ------------
    X: DataFrame
        independent variables
    y: Series or array
        target variable

    return
    ------------
    DataFrame of pearson coefficient and two-tailed p-value for each column in X
    """
    corrs = [pearsonr(X[col], y) for col in X.columns]

    return pd.DataFrame(corrs, columns=['Pearson Coefficient', 'Two-Tailed p-value'], index=X.columns)


def adjusted_r2(r2, n, p):
    """
    r2:
        R^2 of the model
    n:
        data used to get the R^2 of the model
    p: int

    the adjusted R^2
    """
    return 1 - (((1 - r2) * (n - 1)) / (n - p - 1))


def odds(prob):
    """
    return the odds of an event occuring given its probability of occuring
    """
    return prob / (1 - prob)


def log_odds(prob):
    """
    return the log odd of an event occuring given its probablity of occuring
    """
    return np.log(odds(prob))