import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
def first_part():
    df = pd.read_csv(r"D:\ML-Course\08-Linear-Regression-Models\Advertising.csv")
    print(df.head())
    X = df.drop("sales", axis = 1)
    y = df["sales"]


    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3, random_state = 101)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    model = Ridge(alpha = 100)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    MSE = mean_squared_error(y_test, y_pred)
    print(MSE)
    model_two = Ridge(alpha = 1)
    model_two.fit(X_train, y_train)
    y_pred_two = model_two.predict(X_test)
    MSE_two = mean_squared_error(y_test, y_pred_two)
    print(MSE_two)
def second_part():
    df = pd.read_csv(r"D:\ML-Course\08-Linear-Regression-Models\Advertising.csv")
    print(df.head())
    X = df.drop("sales", axis = 1)
    y = df["sales"]

    X_train, X_other, y_train, y_other = train_test_split(X,y,test_size = 0.3, random_state = 101)
    X_val, X_test, y_val, y_test = train_test_split(X_other, y_other, test_size = 0.5, random_state = 101)
    print(len(df))
    print(len(X_train))
    print(len(X_val))
    print(len(X_test))

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)
    model = Ridge(alpha = 100)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    MSE = mean_squared_error(y_val, y_pred)
    print(MSE)
    model_two = Ridge(alpha = 1)
    model_two.fit(X_train, y_train)
    y_pred_two = model_two.predict(X_val)
    MSE_two = mean_squared_error(y_val, y_pred_two)
    print(MSE_two)

    y_final_test_pred = model_two.predict(X_test)
    MSE_final = mean_squared_error(y_final_test_pred, y_test)
    print(MSE_final)
def third_part():
    df = pd.read_csv(r"D:\ML-Course\08-Linear-Regression-Models\Advertising.csv")
    print(df.head())
    X = df.drop("sales", axis=1)
    y = df["sales"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    model = Ridge(alpha=100)
    scores = cross_val_score(model, X_train, y_train, scoring="neg_mean_squared_error", cv=5)
    print(scores)
    model = Ridge(alpha=1)
    scores = cross_val_score(model, X_train, y_train, scoring="neg_mean_squared_error", cv=5)
    print(scores)
    model.fit(X_train, y_train)
    y_final_test_pred = model.predict(X_test)
    MSE_final = mean_squared_error(y_final_test_pred, y_test)
    print(MSE_final)
def fourth_part():
    df = pd.read_csv(r"D:\ML-Course\08-Linear-Regression-Models\Advertising.csv")
    print(df.head())
    X = df.drop("sales", axis=1)
    y = df["sales"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    model = Ridge(alpha=100)
    scores = cross_validate(model, X_train, y_train, scoring=["neg_mean_absolute_error", "neg_mean_squared_error"],
                            cv=10)
    scores = pd.DataFrame(scores)
    pd.set_option('display.width', None)
    print(scores)
    print(scores.mean())
    model = Ridge(alpha=1)
    model.fit(X_train, y_train)
    y_final_pred = model.predict(X_test)
    print(mean_squared_error(y_final_pred, y_test))

df = pd.read_csv(r"D:\ML-Course\08-Linear-Regression-Models\Advertising.csv")
print(df.head())
X = df.drop("sales", axis=1)
y = df["sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

base_elastic_net_model = ElasticNet()
param_grid = {"alpha": [0.1, 1, 5, 50, 100], "l1_ratio": [0.1, 0.5, 0.7, 0.95, 0.99, 1]}
grid_model = GridSearchCV(estimator = base_elastic_net_model, param_grid = param_grid, scoring = "neg_mean_squared_error", cv = 5, verbose = 2)
grid_model.fit(X_train, y_train)
print(grid_model.best_estimator_)
print(grid_model.best_params_)
pd.set_option('display.width', None)
print(pd.DataFrame(grid_model.cv_results_))
y_pred = grid_model.predict(X_test)
print(mean_squared_error(y_test, y_pred))



