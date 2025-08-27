import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"D:\ML-Course\08-Linear-Regression-Models\Advertising.csv")
print(df.head())
df["total_ads"] = df["TV"] + df["radio"] + df["newspaper"]
print(df.head())
##sns.scatterplot(data=df,x="total_ads",y="sales")
##sns.regplot(data=df,x="total_ads",y="sales")
plt.show()
X = df["total_ads"]
y = df["sales"]
betta = np.polyfit(x = X,y = y,deg=1)
b1 = betta[0]
b0 = betta[1]
## y = b1x + b0
print(betta)

def get_predicated_sales(b0, b1, potential_spend):
    predicted_sales = b0 + b1 * potential_spend
    return predicted_sales

potential_spend = np.linspace(0, 500, 100)
predicted_sales_for_potential_spend = get_predicated_sales(b0,b1,potential_spend)
sns.scatterplot(data=df,x="total_ads",y="sales")
plt.plot(potential_spend, predicted_sales_for_potential_spend, color="red")
plt.show()
predicated_sales_for_200 = get_predicated_sales(b0,b1,200)
print(predicated_sales_for_200)
#y = a3 * x^3 + a2 * x^2 + a1 * x + a0
alpha = np.polyfit(X,y,deg=3)
print(alpha)
a = [c for c in alpha[::-1]]
potential_spend = np.linspace(0, 500, 100)
predicted_sales = (a[3] * potential_spend ** 3 + a[2] * potential_spend ** 2 + \
a[1] * potential_spend + a[0])
sns.scatterplot(data=df,x="total_ads",y="sales")
plt.plot(potential_spend, predicted_sales, color="red")
plt.show()


