import pandas as pd

data = {
    "OrderID": [1, 2, 2, 3, 4, None],
    "Customer": ["A", "B", "B", "C", None, "D"],
    "Amount": [100, 200, 200, None, 300, 400]
}

df = pd.DataFrame(data)

df.to_csv("EcommRawData.csv", index=False)


df = pd.read_csv("EcommRawData.csv")
analyzeDf = df.drop_duplicates()
final_output = analyzeDf.dropna()


final_output.to_csv("EcommFilterData.csv", index=False)
