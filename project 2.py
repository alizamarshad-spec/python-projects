import pandas as pd
import csv

data = [
    ["Ingredient", "Qty_kg", "Cost_per_kg"],
    ["Coffee Beans", 10.5, 15.99],
    ["Milk", 25.0, 1.20],
    ["Sugar", 8.0, 2.50],
    ["Chocolate Syrup", 5.0, 8.99],
    ["Whipped Cream", 3.5, 12.50]
]

with open("morning_stock.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def use_item(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            self.quantity = 0
        return self.quantity


df = pd.read_csv("morning_stock.csv")

df = df.rename(columns={"Qty_kg": "Current_Quantity"})
coffee_data = df[df["Ingredient"] == "Coffee Beans"]

name = coffee_data["Ingredient"].values[0]
qty = coffee_data["Current_Quantity"].values[0]

coffee = Ingredient(name, qty)

coffee.use_item(2.5)

df.loc[df["Ingredient"] == "Coffee Beans", "Current_Quantity"] = coffee.quantity


df.to_csv("evening_stock.csv", index=False)

print("Evening stock file saved successfully")
print(df)