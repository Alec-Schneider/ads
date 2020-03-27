import xgboost as xgb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def fit_model(model, X_train, y_train, X_test, y_test, params=None, scoring='rmse',  useCV=True, folds=5, early_stopping_rounds=50, seed=100):
    """
    
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
    test_preds = model.predict(X_test[params].values)
    #train_predprob = model.predict_proba(X[params])[:, 1]
    
    print('Training %s: %.4g' % (scoring ,np.sqrt(mean_squared_error(y_train, train_preds))))
    print('Test %s: %.4g' % (scoring, np.sqrt(mean_squared_error(y_test, test_preds))))
    feat_imp = pd.Series(model.feature_importances_, index=params).sort_values(ascending=False)
    fig = plt.figure(figsize=(12,12))
    feat_imp.plot(kind='bar', title='Feature Importances')
    plt.ylabel('Feature Importance Score')
    plt.xlabel('Feature')
    plt.show()