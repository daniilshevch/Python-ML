import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def first_part():
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
def second_part():
    with open(r"D:\ML-Course\DATA\Ames_Housing_Feature_Description.txt", "r") as f:
        print(f.read())
    df = pd.read_csv(r"D:\ML-Course\DATA\Ames_outliers_removed.csv")
    pd.set_option("display.width", None)
    print(df.head())
    df = df.drop("PID", axis = 1)
    #print(df.info())
    print(len(df.columns))
    print(df.isna())
    print(100 * df.isna().sum() / len(df))

    def percent_missing(df):
        result = 100 * df.isna().sum() / len(df)
        result = result[result>0].sort_values()
        return result
    missing_percentage = percent_missing(df)
    #plt.figure(figsize = (10,6), dpi = 200)
    #sns.barplot(x=missing_percentage.index, y=missing_percentage)
    #plt.xticks(rotation=90)
    #plt.ylim(0,1)
    #plt.show()
    print(missing_percentage[missing_percentage < 1])
    df = df.dropna(axis = 0, subset=["Electrical", "Garage Area"])
    missing_percentage = percent_missing(df)
    print(missing_percentage)

    gar_str_cols = ["Garage Type", "Garage Finish", "Garage Qual", "Garage Cond"]
    df[gar_str_cols] = df[gar_str_cols].fillna("None")
    df["Garage Yr Blt"] = df["Garage Yr Blt"].fillna(0)
    df = df.drop(["Pool QC", "Misc Feature", "Alley", "Fence"], axis = 1)
    print(df["Fireplace Qu"].value_counts())
    df["Fireplace Qu"] = df["Fireplace Qu"].fillna("None")
    print(df["Fireplace Qu"].value_counts())
    print(df["Lot Frontage"])


df = pd.read_csv(r"D:\ML-Course\DATA\Ames_No_Missing_Data.csv")
df["MS SubClass"] = df["MS SubClass"].apply(str)
direction = pd.Series(["Up", "Up", "Down"])
print(pd.get_dummies(direction, drop_first=True))
text_df = df.select_dtypes(include="object")
numeric_df = df.select_dtypes(exclude="object")
df_object_dummies = pd.get_dummies(text_df, drop_first=True)
pd.set_option("display.width", None)
print(df_object_dummies)
final_df = pd.concat([numeric_df, df_object_dummies], axis=1)
print(final_df)



