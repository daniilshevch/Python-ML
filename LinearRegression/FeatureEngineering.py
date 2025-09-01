import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_ages(mu = 50, sigma = 13, num_samples = 100, seed = 42):
    np.random.seed(seed)

    sample_ages = np.random.normal(loc=mu, scale=sigma, size=num_samples)
    sample_ages = np.round(sample_ages, decimals = 0)

    return sample_ages

sample = create_ages()
print(sample)
#sns.displot(sample, bins = 20)
#sns.boxplot(sample)
#plt.show()
ser = pd.Series(sample)
print(ser)
print(ser.describe())
IQR = 55.25 - 42
lower_limit = 42 - 1.5 * IQR
print(lower_limit)
print(ser[ser > lower_limit])
print(ser[ser < lower_limit])

q25, q75 = np.percentile(sample,[25,75])
IQR = q75 - q25
print(q25 - 1.5 * IQR)

df = pd.read_csv(r"D:\ML-Course\DATA\Ames_Housing_Data.csv")
pd.set_option("display.width", None)
print(df)
print(df.corr(numeric_only=True)["SalePrice"])
#sns.scatterplot(x = "Overall Qual", y = "SalePrice", data=df)
#sns.scatterplot(x = "Gr Liv Area", y = "SalePrice", data=df)
print(df[(df["Overall Qual"] > 8) & (df["SalePrice"] < 200000)])
print(df[(df["Gr Liv Area"] > 4000) & (df["SalePrice"] < 200000)])
indexes = df[(df["Gr Liv Area"] > 4000) & (df["SalePrice"] < 200000)].index
print(indexes)
df = df.drop(indexes, axis = 0)
sns.scatterplot(x = "Gr Liv Area", y = "SalePrice", data=df)
plt.show()
df.to_csv("Ames_Outliers_Removed.csv")