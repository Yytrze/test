import pandas as pd

stock1 = pd.Series([120, 80, None , 60, 95, None , 110])

index_labels = ["Apple","Banana","Orange","Mango","Grapes","Peach","Melon"]
stock2 = pd.Series([120, 80, None , 60, 95, None , 110],index=index_labels)

stock3 = stock2.to_dict()

print("Stock1")
print(stock1)
print()

print("Stock2")
print(stock2)
print()

print("Stock3")
print(stock3)
print()

print(f"Banana 庫存:{stock3['Banana']}")
print()

print("缺少值檢查")
print(stock2.isnull())
print()

print(f"缺少值數量:{stock2.isnull().sum()}")

stock2.to_csv("0520_stock.csv",header=["Stock"], index_label="Product")
