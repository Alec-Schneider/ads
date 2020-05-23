import xgboost as xgb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

def fit_xgbr(model, X_train, y_train, params=None, scoring='rmse',  useCV=True, folds=5, early_stopping_rounds=50, seed=100, file_path=None):
    """
    model: XGBRegressor model; required
        path to file
    X_train: DataFrame
        training data
    y_train: DataFrame
        target variable
    params:
        parameters of X_train to use on the bot
    scoring:
            
    """
    if not params:
        params = X_train.columns
    
    if useCV:
        xgb_params = model.get_xgb_params()
        xgtrain = xgb.DMatrix(X_train[params].values, label=y_train.values)
        cvresult = xgb.cv(xgb_params, xgtrain, num_boost_round=model.get_params()['n_estimators'], metrics=scoring, early_stopping_rounds=early_stopping_rounds)
        model.set_params(n_estimators=cvresult.shape[0])
        
    # fit the model on the data
    model.fit(X_train[params].values, y_train.values, eval_metric=scoring)
    
    # predict training set
    train_preds = model.predict(X_train[params].values)
    # metrics = {
    #     'rmse': (mean_squared_error, {'squared': False})
    # }

    if scoring == 'rmse'
        print('Training %s: %.4g' % (scoring , mean_squared_error(y_train, train_preds, squared=False)))
    elif == 'mse':
        print('Training %s: %.4g' % (scoring , mean_squared_error(y_train, train_preds)))
    feat_imp = pd.Series(model.feature_importances_, index=params).sort_values(ascending=False)
    fig = plt.figure(figsize=(12,12))
    feat_imp.plot(kind='bar', title='Feature Importances')
    plt.ylabel('Feature Importance Score')
    plt.xlabel('Feature')
    plt.show()