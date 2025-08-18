import numpy as np
import pandas as pd
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

registrations = pd.DataFrame({"reg_id":[1,2,3,4], "name": ["Andrew", "Bob", "Claire", "David"]})
logins = pd.DataFrame({"log_id": [1,2,3,4], "name": ["Xavier", "Andrew", "Yolanda", "Bob"]})
print(registrations)
print(logins)
mg = pd.merge(registrations, logins, how="inner", on = "name")
print(mg)