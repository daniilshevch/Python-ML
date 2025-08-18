import numpy as np
import pandas as pd
def first_part():
    my_index = ["USA", "Canada", "Mexico"]
    my_data = [1776, 1867, 1821]
    ser = pd.Series(data = my_data, index = my_index)
    ser2 = pd.Series(data = my_data)
    print(ser)
    print(ser2)
    print(ser.iloc[0])
    print(ser.loc["USA"])
    print(ser["USA"])
    ages = {"Petro" : 47, "Misha": 42, "Karl": 34}
    ser = pd.Series(ages)
    print(ser)

    q1 = {"Japan": 80, "China": 450, "India": 200, "USA": 250}
    q2 = {"Brazil": 100, "China": 500, "India": 210, "USA": 260}
    ser1 = pd.Series(data = q1)
    ser2 = pd.Series(q2)
    print(ser1)
    print(ser2)
    print(ser1.keys())
    print(ser2.keys())

    ser1_mod = ser1 * 2
    print(ser1_mod)
    ser1_mod /= 3
    print(ser1_mod)
    print(ser1 + ser2)
    print(ser1.add(ser2, fill_value=0))
    print(ser1.dtype)
    print((ser1 + ser2).dtype)
def second_part():
    np.random.seed(101)
    my_data = np.random.randint(0, 101, (4,3))
    print(my_data)
    print(type(my_data))
    my_index = ["Lviv", "Odesa", "Ivano-Frankivsk", "Lutsk"]
    my_columns = ["September", "October", "November"]
    df = pd.DataFrame(data=my_data)
    print(df)
    df = pd.DataFrame(data=my_data, index=my_index)
    print(df)
    df = pd.DataFrame(data=my_data, index=my_index, columns=my_columns)
    print(df)
    print(df.info())
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    print(df)
    print(df.head(11))
    print(df.tail(3))
def third_part():
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    print(df)
    print(df.columns)
    print(df.index)
    print(df.head())
    print(df.info())
    print(df.describe())
    print(df.describe().transpose())
    print("------------------------")
    print(df["total_bill"])
    print(type(df["total_bill"]))
    new_df = df[["total_bill", "Payer Name", "sex"]]
    print(new_df)
    print(type(new_df))
    df["tips_percentage"] = df["tip"] / df["total_bill"] * 100
    print(df)
    df["tips_percentage"] = np.round(df["tips_percentage"], 2)
    print(df)
    print(df.drop("total_bill", axis=1))
    print(df.shape)
def fourth_part():
    pd.set_option("display.width", None)
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    print(df)
    df = df.set_index("Payment ID")
    print(df)
    # df.reset_index(inplace=True)
    # print(df)
    # df = df.set_index("Payer Name")
    # print(df)
    print(df.iloc[2])
    print(df.iloc[3])
    print(df)
    print(df.loc["Sun5260"])
    print("-------------")
    print(df)
    df.reset_index(inplace=True)
    print(df.iloc[2:16:3])
    df.set_index("Payment ID", inplace=True)
    print("----------")
    print(df.loc[["Sun4458", "Sun6820", "Sun6686"]])
    print(df.drop("Sun4458"))
    first_row = df.iloc[0]
    second_row = df.iloc[1]
    third_row = df.iloc[2]
    print(first_row)
    print(type(first_row))
    df = pd.concat([df, pd.DataFrame([first_row, second_row])])
    df.loc["XXXX"] = third_row
    df.loc["YYYY"] = pd.Series(third_row)
    print(df)
def fifth_part():
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    print(df["tip"] > 3)
    print(type(df["tip"] > 2))
    print(df[df["tip"] > 3])
    pd.set_option("display.max_rows", None)
    pd.set_option("display.width", None)
    print(df["total_bill"] > 40)
    print(df[df["total_bill"] > 40])
    print("----------------------------")
    print(df[ (df["total_bill"] > 40) & (df["tip"] > 5) ])
    print(df.head())
    print(df[(df["day"] == "Sun") | (df["day"] == "Sat") | (df["day"] == "Fri")])
    print("---------------")
    print(df[df["day"].isin(["Fri", "Sat"])])
def sixth_part():
    def get_last_four_digits(number):
        return int(str(number)[-4:])
    def define_category(total_bill):
        if total_bill > 30:
            return "Expensive"
        elif total_bill > 20:
            return "Average"
        else:
            return "Cheap"

    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    print(df.head())
    df["last four"] = df["CC Number"].apply(get_last_four_digits)
    print(df)
    print(df["total_bill"])
    df["category"] = df["total_bill"].apply(define_category)
    pd.set_option("display.max_rows", None)
    print(df)
def seventh_part():
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    print(df.head())
    df["double_bill"] = df["total_bill"].apply(lambda total_bill: total_bill * 2)
    print(df)
    def quality_of_tip(total_bill, tip):
        if tip / total_bill > 0.25:
            return "Excellent"
        else:
            return "General"
    df["quality_of_tip"] = df[["total_bill", "tip"]].apply(lambda row: quality_of_tip(row["total_bill"], row["tip"]), axis = 1)
    pd.set_option("display.max_rows", None)
    df["quality_of_tip2"] = np.vectorize(quality_of_tip)(df["total_bill"], df["tip"])
    print(df)
def ninth_part():
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    print(df.describe())
    print(df.sort_values("total_bill"))
    print(df.sort_values("total_bill", ascending=False))
    print(df.sort_values(["tip", "total_bill"], ascending=[True, False]))
    pd.set_option("display.max_rows", None)
    print(df["total_bill"])
    print(df["total_bill"].max())
    print(df["total_bill"].idxmax())
    print(df.iloc[170])
    print(df.corr(numeric_only=True))
    print(df["sex"].value_counts())
    print(df["day"])
    print(df["day"].unique())
    print(df["day"].nunique())
    ##df["sex"] = df["sex"].replace(["Female", "Male"], ["F", "M"])
    print(df)
    my_map = {"Female": "F", "Male": "M"}
    print(df["sex"].map(my_map))
    print(df.duplicated())
    simple_df = pd.DataFrame(data=[1,2,2,2], index=["a","b","c","d"], columns = ["value"])
    print(simple_df)
    print(simple_df.duplicated())
    print(simple_df.drop_duplicates())
    print(simple_df["value"])
    print(type(simple_df["value"]))
    print(df["total_bill"].between(10,20, inclusive="both"))
    print(df[df["total_bill"].between(10,20, inclusive="both")])
    print(df.nlargest(10, "tip"))
    print("----------------------------------------")
    print(df.sort_values("tip", ascending=False).iloc[0:10])
    print(df.sample(6))
def tenth_part():
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\movie_scores.csv")
    my_var = np.nan
    print(my_var == np.nan)
    print(my_var is np.nan)
    print(df)
    print(df.isnull())
    print(df["pre_movie_score"].notnull())
    print(df[df["pre_movie_score"].notnull()])
    print(df[ (df["pre_movie_score"].isnull()) & (df["first_name"].notnull()) ])
    print("-----------------------")
    print(df)
    print(df.dropna())
    print(df.dropna(thresh=4))
    print(df.dropna(axis = 1))
    print(df.dropna(subset=["last_name"]))
    print(df.fillna("New Value"))
    df["pre_movie_score"] = df["pre_movie_score"].fillna(0)
    df["post_movie_score"] = df["post_movie_score"].fillna(-1)
    print(df)
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\movie_scores.csv")
    df["pre_movie_score"] = df["pre_movie_score"].fillna(df["pre_movie_score"].mean())
    print(df)

    airline_tix = {"first": 100, "business": np.nan,"economy-plus":50, "economy": 30}
    ser = pd.Series(airline_tix)
    print(ser)
    print(ser.interpolate())
    print(ser["first"])
    print(ser.loc["first"])
    print(ser.iloc[0])

df = pd.read_csv(r"D:\ML-Course\03-Pandas\mpg.csv")
pd.set_option("display.width", None)
print(df)
df["model_year"] += 1900
print(df)
print(df["model_year"].unique())
print(df["model_year"].value_counts().sort_values(ascending=True))
print(df.groupby("model_year").mean(numeric_only=True))
print("---------------------------")
print(df.groupby(["model_year", "cylinders"]).mean(numeric_only=True).index)
print("------------------")
grouped_df = df.groupby("model_year").mean(numeric_only=True)
print(grouped_df)
print(grouped_df.loc[1979])
print(grouped_df.loc[[1979, 1982]])

year_cyl = df.groupby(["model_year", "cylinders"]).mean(numeric_only=True)
print(year_cyl)
print(year_cyl.index.names)
print(year_cyl.loc[1970])
print(year_cyl.loc[[1971,1978]])
print(year_cyl.loc[1970])
print(year_cyl.loc[(1970, 4)])
print(year_cyl)
print(year_cyl.xs(key=1970, level = "model_year"))
print(year_cyl.xs(key=4, level="cylinders"))
test = df[df["cylinders"].isin([6,8])].groupby(["model_year", "cylinders"]).mean(numeric_only=True)
print(test)
print(year_cyl)
print(year_cyl.swaplevel())
test = df.sort_values(["model_year", "cylinders"], ascending=[True, False])
print(test.groupby(["model_year", "cylinders"], sort=False).mean(numeric_only=True))
print(df.agg())