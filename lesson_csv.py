
import pandas as pd

l_connections = [
    {
        "name": "zekken",
        "password": "123"
    },
    {
        "name": "test_user",
        "password": "456"
    }
]

df1 = pd.DataFrame(l_connections)
print(df1)

df1.to_csv("from_pandas.csv", index=False)

df2 = pd.read_csv("from_pandas.csv")
print(df2)