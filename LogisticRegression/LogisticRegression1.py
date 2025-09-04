import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
def first_part():
    df = pd.read_csv(r"D:\ML-Course\DATA\hearing_test.csv")
    print(df.head())
    print(df["test_result"].value_counts())
    ##sns.countplot(x="test_result", data=df)
    ##sns.boxplot(x="test_result", y = "age", data =df)
    ##sns.boxplot(x="test_result", y = "physical_score", data =df)
    ##sns.scatterplot(x="age", y = "physical_score", data=df, hue = "test_result")
    sns.pairplot(df,hue="test_result")
    plt.show()
def second_part():
    df = pd.read_csv(r"D:\ML-Course\DATA\hearing_test.csv")
    X = df.drop("test_result",axis=1)
    y = df["test_result"]
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=101)
    scaler = StandardScaler()
    scaled_X_train = scaler.fit_transform(X_train)
    scaled_X_test = scaler.transform(X_test)
    from sklearn.linear_model import LogisticRegression
    log_model = LogisticRegression()
    log_model.fit(scaled_X_train, y_train)
    print(log_model.coef_)
    y_pred = log_model.predict(scaled_X_test)
    print(y_pred)
    y_pred_probability = log_model.predict_proba(scaled_X_test)
    print(y_pred_probability)
    print(log_model.coef_)
    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
    print(y_test)
    y_pred = log_model.predict(scaled_X_test)
    print(y_pred)
    print(accuracy_score(y_test, y_pred))
    matrix = confusion_matrix(y_test, y_pred)
    print(matrix)
    from sklearn.metrics import ConfusionMatrixDisplay
    ConfusionMatrixDisplay.from_estimator(log_model, scaled_X_test, y_test, normalize='all')
    plt.show()
    print(y_test[0])
    print(y_pred[0])
    print(y_pred_probability[0])

df = pd.read_csv(r"D:\ML-Course\DATA\iris.csv")
print(df.head())
print(df.info())
print(df["species"].value_counts())
##sns.countplot(x="species", data=df)
##sns.scatterplot(x="petal_length", y="petal_width", data=df, hue="species")
##sns.pairplot(df, hue="species")

plt.show()
X = df.drop("species",axis=1)
y = df["species"]
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)
scaler = StandardScaler()
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)
