import pandas as pd
data = {
    "Customer_name":["Akash" , "Nikhil","Sachin"],
    "Customer_address" : ["Jaunpur", "Azamgrah" , "jammu"],
    "Customer_age" : [20,23,10],
    "customer_gender" : ['M','M','M']
}
df = pd.DataFrame(data)
df.to_csv("file.csv")