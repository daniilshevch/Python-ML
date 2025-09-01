import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression

from LinearRegression3 import test_predictions

def first_part():
    df = pd.read_csv(r"D:\ML-Course\08-Linear-Regression-Models\Advertising.csv")
    print(df.head())
    X = df.drop("sales", axis = 1)
    y = df["sales"]
    polynomial_converter = PolynomialFeatures(degree=3,include_bias=False)
    poly_features = polynomial_converter.fit_transform(X)
    print(poly_features.shape)
    X_train, X_test, y_train, y_test = train_test_split(poly_features,y,test_size=0.3, random_state=101)
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    from sklearn.linear_model import Ridge
    ridge_model = Ridge(alpha = 10)
    ridge_model.fit(X_train,y_train)
    test_predictions = ridge_model.predict(X_test)
    from sklearn.metrics import mean_absolute_error, mean_squared_error
    MAE = mean_absolute_error(y_test, test_predictions)
    print(MAE)
    RMSE = np.sqrt(mean_squared_error(y_test, test_predictions))
    print(RMSE)
    from sklearn.linear_model import RidgeCV
    from sklearn.metrics import get_scorer_names
    ridge_cv_model = RidgeCV(alphas=(0.1, 1.0, 10.0), scoring="neg_mean_absolute_error")
    ridge_cv_model.fit(X_train,y_train)
    print(ridge_cv_model.alpha_)
    test_predictions = ridge_cv_model.predict(X_test)
    MAE = mean_absolute_error(y_test, test_predictions)
    print("--------")
    print(MAE)
    RMSE = np.sqrt(mean_squared_error(y_test, test_predictions))
    print(RMSE)
    print(ridge_cv_model.coef_)

df = pd.read_csv(r"D:\ML-Course\08-Linear-Regression-Models\Advertising.csv")
print(df.head())
X = df.drop("sales", axis = 1)
y = df["sales"]
polynomial_converter = PolynomialFeatures(degree=3,include_bias=False)
poly_features = polynomial_converter.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=101)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
from sklearn.linear_model import LassoCV
lasso_cv_model = LassoCV(eps=0.1,alphas=100)
lasso_cv_model.fit(X_train, y_train)
print(lasso_cv_model.alpha_)
test_predictions = lasso_cv_model.predict(X_test)
MAE = mean_absolute_error(y_test, test_predictions)
print("--------")
print(MAE)
RMSE = np.sqrt(mean_squared_error(y_test, test_predictions))
print(RMSE)
print(lasso_cv_model.coef_)
from sklearn.linear_model import ElasticNetCV
elastic_cv_model = ElasticNetCV(l1_ratio=[0.1, 0.5,0.7,0.9, 0.95, 0.99, 1], eps=0.001,alphas=100, max_iter = 1000000)
elastic_cv_model.fit(X_train, y_train)
print(elastic_cv_model.alpha_)
print(elastic_cv_model.l1_ratio)
print(elastic_cv_model.l1_ratio_)
test_predictions = elastic_cv_model.predict(X_test)
MAE = mean_absolute_error(y_test, test_predictions)
print("--------")
print(MAE)
RMSE = np.sqrt(mean_squared_error(y_test, test_predictions))
print(RMSE)