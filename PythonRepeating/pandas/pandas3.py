import numpy as np
import pandas as pd
from datetime import datetime
import os
def first_part():
    data_one = {"A": ["A0", "A1", "A2", "A3"], "B": ["B0", "B1", "B2", "B3"]}
    data_two = {"C": ["C0", "C1", "C2", "C3"], "D": ["D0", "D1", "D2", "D3"]}
    one = pd.DataFrame(data_one)
    two = pd.DataFrame(data_two)
    print(one)
    df = pd.concat([one, two], axis=1)
    print(df)
    print(df.loc[0])
    print(df.loc[0,"C"])
    print(df.loc[2, "B"])
    print(pd.concat([one,two]))
    two.columns = one.columns
    print(two)
    my_df = pd.concat([one,two])
    print(my_df)
    my_df.index = np.arange(len(my_df))
    print(my_df)
    print(two.columns)
    two.columns.values[0] = "XXX"
    two.columns.values[1] = "YYY"
    print(two)
def second_part():
    registrations = pd.DataFrame({"reg_id":[1,2,3,4], "name": ["Andrew", "Bob", "Claire", "David"]})
    logins = pd.DataFrame({"log_id": [1,2,3,4], "name": ["Xavier", "Andrew", "Yolanda", "Bob"]})
    print(registrations)
    print(logins)
    mg = pd.merge(registrations, logins, how="inner", on = "name")
    print(mg)
    md = pd.merge(left = registrations, right = logins, how="left", on = "name")
    print(md)
    md = pd.merge(registrations, logins, how = "right", on = "name")
    print(md)
    md = pd.merge(registrations, logins, how = "outer", on = "name")
    print(md)
def third_part():
    registrations = pd.DataFrame({"reg_id":[1,2,3,4], "name": ["Andrew", "Bob", "Claire", "David"]})
    logins = pd.DataFrame({"log_id": [1,2,3,4], "name": ["Xavier", "Andrew", "Yolanda", "Bob"]})
    registrations.set_index("name", inplace=True)
    print(registrations)
    print(logins)
    df = pd.merge(registrations, logins, left_index=True, right_on="name", how="inner")
    print(df)
    registrations.reset_index(inplace=True)
    registrations.columns = ["reg_name", "reg_id"]
    print(registrations)
    print(logins)
    df = pd.merge(registrations, logins, left_on="reg_name", right_on="name", how="inner")
    print(df.drop("reg_name", axis = 1))
    registrations.columns = ["name", "id"]
    print(registrations)
    logins.columns = ["id", "name"]
    print(logins)
    df = pd.merge(registrations, logins, on="name", how="inner", suffixes = ("_reg", "_log"))
    print(df)
def fourth_part():
    email = "daniil_shevchenko@gmail.com"
    names = pd.Series(["Andrew", "Bob", "Claire", "David", "5", "23"])
    print(names)
    print(names.str.upper())
    print(names.str.isdigit())
    print(names[names.str.isdigit()])

    tech_finance = ["GOOG,APPL,AMZN", "JPN,BAC,GS"]
    tickers = pd.Series(tech_finance)
    print(tickers)
    print(tickers.str.split(",", expand = True))
    messy_names = pd.Series(["andrew  ", "Bo:bo"," Claire  "])
    print(messy_names)
    print(messy_names.str.replace(":", "").str.strip().str.capitalize())
    def clean_up(name):
        name = name.replace(":", "")
        name = name.strip()
        name = name.capitalize()
        return name
    print(messy_names.apply(clean_up))
def fifth_part():
    my_year = 2025
    my_month = 8
    my_day = 19
    my_hour = 10
    my_min = 34
    my_date = datetime(my_year, my_month, my_day)
    print(my_date)
    my_date = datetime(my_year, my_month, my_day, my_hour, my_min)
    print(my_date)
    my_ser = pd.Series(["Nov 3, 1990", "2000-01-01", None])
    print(my_ser)
    df = pd.to_datetime(my_ser, format="mixed")
    print(df)
    print(df[1])
    obvious_euro_date = "31-12-2000"
    print(pd.to_datetime(obvious_euro_date, dayfirst=True))
    style_date = "22--Dec--2000"
    print(pd.to_datetime(style_date,format='%d--%b--%Y'))
    custom_date = "12th of Dec 2000"
    print(pd.to_datetime(custom_date))
    sales = pd.read_csv(r"D:\ML-Course\03-Pandas\RetailSales_BeerWineLiquor.csv")
    print(sales)
    print(sales["DATE"])
    sales["DATE"] = pd.to_datetime(sales["DATE"])
    print(sales["DATE"])
    sales = pd.read_csv(r"D:\ML-Course\03-Pandas\RetailSales_BeerWineLiquor.csv", parse_dates = ["DATE"])
    print(sales.info())
    print(sales["DATE"].dt.year)
print(os.getcwd())
df = pd.read_csv(r"D:\ML-Course\03-Pandas\example.csv")
print(df)
df.to_csv("test.csv", index=False)

df = pd.read_excel(r"D:\ML-Course\03-Pandas\my_excel_file.xlsx", sheet_name = "First_Sheet")
print(df)
wb = pd.ExcelFile(r"D:\ML-Course\03-Pandas\my_excel_file.xlsx")
print(wb.sheet_names)

excel_sheet_dict = pd.read_excel(r"D:\ML-Course\03-Pandas\my_excel_file.xlsx", sheet_name = None)
print(type(excel_sheet_dict))
print(excel_sheet_dict.keys())
print(excel_sheet_dict["First_Sheet"])

df.to_excel("test.xlsx", sheet_name = "Test Sheet")



