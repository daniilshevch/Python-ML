import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.core.internals.construction import rec_array_to_mgr
df = pd.read_csv(r"D:\ML-Course\08-Linear-Regression-Models\Advertising.csv")
print(df.head())
# fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16,6))
# axes[0].plot(df["TV"], df["sales"], "o")
# axes[0].set_title("TV Spend")
# axes[0].set_ylabel("Sales")
#
# axes[1].plot(df["radio"], df["sales"], "o")
# axes[1].set_title("Radio Spend")
# axes[1].set_ylabel("Sales")
#
# axes[2].plot(df["newspaper"], df["sales"], "o")
# axes[2].set_title("Newspaper Spend")
# axes[2].set_ylabel("Sales")

#plt.show()

##sns.pairplot(data=df)
#plt.show()

X = df.drop("sales", axis = 1)
print(X.head())
y = df["sales"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)
print(len(X_train))
print(len(X))
print(X_train)
print(y_train)
print(type(y_train))

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
print(model.coef_)
print(model.intercept_)
test_predictions = model.predict(X_test)
print(X_test)
print("-----------")
print(y_test)
print("#################")
print(test_predictions[0:5])
print(y_test[0:5])
from sklearn.metrics import mean_absolute_error, mean_squared_error
print(df["sales"].mean())
#sns.histplot(data=df, x="sales", bins=20)
#plt.show()
print(mean_absolute_error(y_test, test_predictions))
print(mean_squared_error(y_test, test_predictions))
print(np.sqrt(mean_squared_error(y_test, test_predictions)))

