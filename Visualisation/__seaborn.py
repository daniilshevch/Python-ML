import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def first_part():
    df = pd.read_csv(r"D:\ML-Course\05-Seaborn\dm_office_sales.csv")
    print(df.head())
    plt.figure(figsize=(12,4), dpi=200)
    #sns.scatterplot(data=df, x = "salary", y = "sales", size = "work experience", style="level of education")
    sns.scatterplot(data=df, x = "salary", y = "sales", hue = "level of education", style="level of education")
    ##sns.scatterplot(data=df, x = "sales", y = "salary")
    plt.savefig("seaborn1.png")
    plt.show()
def second_part():
    df = pd.read_csv(r"D:\ML-Course\05-Seaborn\dm_office_sales.csv")
    print(df.head())
    ##sns.rugplot(data=df, x="salary")
    sns.set_style("darkgrid")
    sns.displot(data=df, x="salary", bins=100, color = "orange", kde=True)
    plt.show()
def third_part():
    df = pd.read_csv(r"D:\ML-Course\05-Seaborn\dm_office_sales.csv")
    print(df.head())
    print(df["division"].value_counts())
    plt.figure(figsize=(10,4), dpi=200)
    ##plt.ylim(90,260)
    ##sns.countplot(data=df, x="division")
    ##sns.countplot(data=df,x="level of education",hue="division", palette="Set2")
    sns.barplot(data=df, x = "level of education", y = "salary", estimator=np.mean, errorbar="sd", hue="division")
    plt.show()


df = pd.read_csv(r"D:\ML-Course\05-Seaborn\StudentsPerformance.csv")
pd.set_option("display.width", None)
print(df.head())
plt.figure(figsize=(10,4), dpi=200)
##sns.boxplot(data=df, y="reading score", x = "parental level of education", hue="test preparation course")
##sns.violinplot(data=df, y="reading score", x = "parental level of education", hue="test preparation course")
sns.swarmplot(data=df,x="math score", y="gender", hue="test preparation course", dodge=True)
plt.show()

