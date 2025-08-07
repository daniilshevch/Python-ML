import numpy as np
import pandas as pd
def first_part():
    index = ["Lviv", "Odesa", "Ternopil"]
    data = [0.9, 1, 0.25]
    series = pd.Series(data = data, index = index)
    print(series)
    print(series.iloc[0])
    print(series["Lviv"])
    print(series.loc["Lviv"])
    print(series.iat[1])
    print(series["Odesa"])
    print(series.at["Odesa"])

    people = {"Petro": 44, "Karl": 29, "Volodymyr": 33}
    series = pd.Series(people)
    print(series)

    q1 = {"Japan":80, "China":450, "India":200, "USA":250}
    q2 = {"Brazil":100, "China":500, "India":210, "USA":260}

    ser1 = pd.Series(q1)
    ser2 = pd.Series(q2)

    print(ser1)
    print("----")
    print(ser2)
    print(ser1["USA"])
    print(ser1.keys())
    print(ser1)
    print(ser1 * 4)
    print("-----------------")
    print(ser1 + ser2)
    print(ser1.add(ser2, fill_value=0))
def second_part():
    np.random.seed(101)
    my_data = np.random.randint(0, 101, (4,3))
    print(my_data)

    my_index = ["Lviv", "Odesa", "Ternopil", "Lutsk"]
    my_columns = ["Jun", "Jul", "Aug"]
    df = pd.DataFrame(my_data)
    print(df)
    df = pd.DataFrame(my_data, index = my_index)
    print(df)
    df = pd.DataFrame(data=my_data, index=my_index, columns=my_columns)
    print(df)
    print(df.info())
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    pd.set_option('display.max_rows', 300)
    pd.set_option('display.width', None)
    print("--------------")
    print(df)
    print(df.columns)
    print(df.index)
    print(df.head(10))
    print("--------------")
    print(df.tail())
    print(df.info())
    print(df.describe())
    print(df.describe().transpose())
def third_part():
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    print(df.head())

    print(df["total_bill"])
    my_cols = ["total_bill", "tip"]
    print(df[my_cols])
    print(df[["total_bill", "tip"]])
    print("-------------")
    print(df)
    print(df["tip"] + df["total_bill"])
    df["percentage"] =  df["tip"] / df["total_bill"] * 100
    print(df)
    df["Payment ID"] = df["total_bill"].astype(str) + df["sex"]
    ##pd.set_option('display.width', None)
    print(df)
    df["percentage"] = np.round(df["percentage"], 2)
    print(df)
    df = df.drop("percentage", axis=1)
    print(df)
def fourth_part():
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    print(df.head())

    df.set_index("Payment ID", inplace=True)
    print(df)
    df.reset_index(inplace=True)
    print(df)
    df.set_index("Payment ID", inplace=True)
    print("xxxxxxxxxxxxxxxxxxx")
    print(df)
    print(df["total_bill"])
    print("----------------------")
    print(df.iloc[3])
    print(df.loc["Sun5260"])
    print("!!!!!!!!!!")
    df.reset_index(inplace=True)
    print(df.iloc[2:9:2])
    df.set_index("Payment ID", inplace=True)
    print(df.loc[["Sun2251", "Sun5985"]])
    df.drop("Sun2251", axis=0, inplace=True)
    print(df)
    one_row = df.iloc[0]
    print(one_row)
    df.loc["xxxxxxx"] = one_row
    print(df)
def fifth_part():
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    print(df.head())
    print(df["total_bill"])
    print(df["total_bill"] > 40)
    print(df[df["total_bill"] > 40])
    print("-----------")
    print(df[df["tip"] > 3.5])
    print("---------------")
    pd.set_option('display.width', None)
    print(df[(df["total_bill"] > 30) & (df["sex"] == "Male")])
    ##pd.set_option('display.max_rows', 300)
    print(df[(df["tip"] < 2) | (df["tip"] > 5)])
    print(df[df["day"].isin(["Fri", "Sat", "Sun"])])
    print(df["day"])
    print(df.iloc[4])
def sixth_part():
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    print(df.iloc[2:6])
    def last_four_symbols(num):
        return str(num)[-4:]
    def define_category(total_bill):
        if(total_bill >= 20):
            return "$$$"
        elif(15 <= total_bill < 20):
            return "$$"
        else:
            return "$"
    print(last_four_symbols(342534534534))
    df["Last four"] = df["CC Number"].apply(last_four_symbols)
    print(df)
    print("------------------------")
    df["category"] = df["total_bill"].apply(define_category)
    print(df)
    print("------------------")
    doubler = lambda n: n * 2
    df["double_total_bill"] = df["total_bill"].apply(doubler)
    print(df)

    def tip_percentage(total_bill, tip):
        return (tip / total_bill) * 100
    def quality_of_tip(total_bill, tip):
        percentage = tip / total_bill
        if(percentage > 0.2):
            return "Excellent"
        elif(percentage > 0.15):
            return "Good"
        else:
            return "General"
    df["tip_percentage"] = df[["total_bill", "tip"]].apply(lambda df: tip_percentage(df["total_bill"], df["tip"]), axis=1)
    df["quality_of_tip"] = df[["total_bill", "tip"]].apply(lambda df: quality_of_tip(df["total_bill"], df["tip"]), axis=1)
    df["quality"] = np.vectorize(quality_of_tip)(df["total_bill"], df["tip"])
    print(df)
def seventh_part():
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\tips.csv")
    print(df.describe())
    print(df.describe().transpose())
    print(df)
    print(df.sort_values(by="total_bill", ascending=False))
    print(df.sort_values(by=["tip", "total_bill"], ascending=[True, False]))
    print("-----------")
    print(df["total_bill"].max())
    print(df["total_bill"].idxmax())
    print(df.iloc[df["total_bill"].idxmax()])
    print(df["sex"].value_counts())
    print(df["day"].unique())
    print(df["day"].nunique())
    print(df["day"].value_counts())
    print("##############################")
    print(df)
    ##df["sex"] = df["sex"].replace(["Female", "Male"], ["F", "M"])
    print(df)
    my_map = {"Female": "F", "Male": "M"}
    df["sex"] = df["sex"].map(my_map)
    print(df)

    print(df.duplicated())
    simple_df = pd.DataFrame([1,2,2,2], ["a", "b", "c", "d"], columns=["letter"])
    print(simple_df)
    print(simple_df.duplicated())
    simple_df = simple_df.drop_duplicates()
    print(simple_df)
    ##pd.set_option('display.max_rows', None)
    print(df["total_bill"].between(18, 22, inclusive="both"))
    print(df[df["total_bill"].between(18, 22, inclusive="both")])
    print(df.nlargest(5, columns=["total_bill"]))
    print(df.sort_values(by="total_bill", ascending=False).iloc[0:5])
    print(df.sample(n=5))
def eighth_part():
    print(np.nan)
    print(pd.NA)
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\movie_scores.csv")
    print(df)
    print(df.isnull())
    print(df.isna())
    print(df[df["pre_movie_score"].notnull()])
    print(df[df["pre_movie_score"].notnull()]["post_movie_score"])
    pre_movie_score_is_null = df["pre_movie_score"].isna()
    print(pre_movie_score_is_null)
    first_name_is_not_null = df["first_name"].notna()
    print(first_name_is_not_null)
    print(df[pre_movie_score_is_null & first_name_is_not_null])
    print("--------")
    print(df)
    print(df.dropna())
    print(df.dropna(thresh=4))
    print(df.dropna(axis=1))
    print(df.dropna(subset=["last_name"]))
    ##df["pre_movie_score"] = df["pre_movie_score"].fillna(0)
    ##df["pre_movie_score"] = df["pre_movie_score"].fillna(df["pre_movie_score"].mean())
    df.loc[df["pre_movie_score"].isna(), "pre_movie_score"] = df["pre_movie_score"].mean()
    print(df)

    airline_tix = {"first":100, "business":np.nan, "economy-plus":50, "economy": 30}
    ser = pd.Series(airline_tix)
    print(ser)
    print(ser.interpolate())
    ser.loc["business"] = 70
    print(ser)
