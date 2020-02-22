from scipy.stats import pearsonr


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


def adjusted_r2(r2, X):
    """
    r2:
        R^2 of the model
    X:
        data used to get the R^2 of the model

    the adjusted R^2
    """
    n, p = X.shape
    return 1 - (((1 - r2) * (n - 1)) / (n - p - 1))