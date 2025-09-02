import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

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

df = pd.read_csv(r"D:\ML-Course\08-Linear-Regression-Models\Advertising.csv")
print(df.head())
X = df.drop("sales", axis = 1)
y = df["sales"]