import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
def first_part():
    df = pd.read_csv(r"D:\ML-Course\08-Linear-Regression-Models\Advertising.csv")
    print(df.head())
    X = df.drop("sales", axis = 1)
    y = df["sales"]
    print(X)
    print(y)
    polynomial_converter = PolynomialFeatures(degree=2, include_bias=False)
    polynomial_converter.fit(X)
    poly_features = polynomial_converter.transform(X)
    print("-----")
    print(poly_features)
    print(X.iloc[0])
    print(poly_features[0])
    X_train, X_test, y_train, y_test = train_test_split(poly_features,y, test_size=0.3, random_state=101)
    model = LinearRegression()
    model.fit(X_train, y_train)
    test_predictions = model.predict(X_test)
    print("###############")
    print(model.coef_)
    print(model.intercept_)
    MAE = mean_absolute_error(y_test, test_predictions)
    MSE = mean_squared_error(y_test, test_predictions)
    RMSE = np.sqrt(MSE)
    print(MAE)
    print(RMSE)

df = pd.read_csv(r"D:\ML-Course\08-Linear-Regression-Models\Advertising.csv")
print(df.head())
X = df.drop("sales", axis = 1)
y = df["sales"]
train_rmse_errors = []
test_rmse_errors = []
for degree in np.arange(1,10):
    poly_converter = PolynomialFeatures(degree=degree, include_bias=False)
    poly_features = poly_converter.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(poly_features,y, test_size=0.3, random_state=101)
    model = LinearRegression()
    model.fit(X_train, y_train)
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_rmse = np.sqrt(mean_squared_error(y_train, train_predictions))
    test_rmse = np.sqrt(mean_squared_error(y_test, test_predictions))
    train_rmse_errors.append(train_rmse)
    test_rmse_errors.append(test_rmse)

print(train_rmse_errors)
print(test_rmse_errors)
plt.plot(np.arange(1,6), train_rmse_errors[:5], label="Train RMSE")
plt.plot(np.arange(1,6), test_rmse_errors[:5], label="Test RMSE")
plt.legend()
plt.show()

final_poly_converter = PolynomialFeatures(degree=3, include_bias=False)
final_model = LinearRegression()
full_converted_X = final_poly_converter.fit_transform(X)
final_model.fit(full_converted_X, y)
from joblib import dump, load
dump(final_model, "final_poly_model.joblib")
dump(final_poly_converter, "final_poly_converter.joblib")

loaded_converter = load("final_poly_converter.joblib")
loaded_model = load("final_poly_model.joblib")

campaign = [[149, 22, 12]]
transformed_data = loaded_converter.transform(campaign)
print(loaded_model.predict(transformed_data))