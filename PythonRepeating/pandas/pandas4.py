import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
def first_part():
    engine = create_engine("mysql+pymysql://root:Mansion20051505@localhost/pandas")
    df = pd.DataFrame(data = np.random.randint(low = 0, high = 100, size = (4,4)), columns = ["a", "b", "c", "d"])
    print(df)
    print(pd.read_sql("new_table", con=engine))
    print(pd.read_sql("users", con=engine))
    print(pd.read_sql_query("select b,d from new_table;", con=engine))
def second_part():
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\Sales_Funnel_CRM.csv")
    pd.set_option("display.width", None)
    print(df)
    licenses = df[["Company", "Licenses", "Product"]]
    print(licenses)
    pv_df = pd.pivot(data=licenses, index="Company", columns = "Product", values = "Licenses")
    print(pv_df)
    print(df)
    print(pd.pivot_table(df, index="Company", aggfunc="sum", values=["Licenses", "Sale Price"]))
    print(df.groupby("Company").sum())
    print(pd.pivot_table(df, index=["Account Manager", "Contact"], values="Sale Price",aggfunc="sum"))
def third_part():
    df = pd.read_csv(r"D:\ML-Course\03-Pandas\hotel_booking_data.csv")
    pd.set_option("display.width", None)
    print(df.head())
    print(len(df))
    print(df.isna())
    print(df.isna().sum())
    print(df.columns)
    print(df.drop("company", axis=1))
    print(df["country"].value_counts())
    print(df.groupby("country").count().sort_values("hotel", ascending=False))
    print(df.sort_values("adr", ascending=False).iloc[:,23:])
    print(df.sort_values("adr", ascending=False)["name"])
    print(df.sort_values("adr", ascending=False)["name"].iloc[0])

    print(df.iloc[df["adr"].idxmax()])
    print(df["adr"].mean())

df = pd.read_csv(r"D:\ML-Course\03-Pandas\hotel_booking_data.csv")
pd.set_option("display.width", None)
print(df.head())
df["total_nights"] = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]
print(df.head())
print(np.round(df["total_nights"].mean(), 2))
df["total_sum_price"] = df["total_nights"] * df["adr"]
print(df.iloc[:,-1:])
print(df["total_sum_price"].mean())
print(df[df["total_of_special_requests"] == 5][["name", "email", "total_of_special_requests"]])
repeated_guest_amount = len(df[df["is_repeated_guest"] == True])
total_guest_amount = len(df)
print(f"{repeated_guest_amount / total_guest_amount * 100} % ")
###
print(df["is_repeated_guest"] == True)
rep = (df["is_repeated_guest"] == True).sum()
print(rep)
total = len(df)
print(type(rep))
print(rep / total)

def get_surname(full_name):
    words = full_name.split()
    return words[1]
df["surname"] = df["name"].apply(get_surname)
print(df)
print(df["surname"].value_counts()[:5])
df["total_children"] = df["babies"] + df["children"]
print(df.sort_values("total_children", ascending=False)[["name", "total_children"]])
df["phone_code"] = df["phone-number"].apply(lambda number: number[:3])
print(df["phone_code"].value_counts()[:5])
print(df.groupby("phone_code").count().sort_values("hotel", ascending=False))
print(df[df["arrival_date_day_of_month"].between(1,15, inclusive="both")][["name", "arrival_date_day_of_month"]].sort_values("arrival_date_day_of_month", ascending=True))
print("------------------")
print(df[df["arrival_date_day_of_month"].apply(lambda day: day in range (1, 16))][["name", "arrival_date_day_of_month"]].sort_values("arrival_date_day_of_month", ascending=True))
df["full_date"] = pd.to_datetime(df["arrival_date_day_of_month"].astype(str) + " " + df["arrival_date_month"] + " " +
                                 df["arrival_date_year"].astype(str))
df["day_of_week"] = df["full_date"].dt.day_name()
print(df)
print(df["day_of_week"].value_counts())
def convert(day, month, year):
    return f"{day}-{month}-{year}"
df["full_date_2"] = np.vectorize(convert)(df["arrival_date_day_of_month"], df["arrival_date_month"], df["arrival_date_year"])
df["full_date_3"] = df[["arrival_date_day_of_month", "arrival_date_month", "arrival_date_year"]].apply(lambda row: convert(row["arrival_date_day_of_month"], row["arrival_date_month"], row["arrival_date_year"]), axis=1)
print(df)
