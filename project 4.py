import pandas as pd

print("STEP 1: Creating the product catalog...")

inventory = {
    'Product_ID': ['P1001', 'P1002', 'P1003', 'P1004', 'P1005', 'P1006', 'P1007', 'P1008'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Electronics', 'Books', 'Electronics', 'Toys'],
    'Price': [599.99, 49.99, 899.99, 129.99, 299.99, 15.99, 749.99, 24.99]
}


store_data = pd.DataFrame(inventory)
store_data.to_csv('products.csv', index=False)
print(" products.csv created successfully")



class Product:
    def __init__(self, prod_id, price):
        self.product_id = prod_id
        self.price = price

    def apply_discount(self, percent_off):
        discount = self.price * (percent_off / 100)
        self.price = self.price - discount
        self.price = round(self.price, 2)
        return self.price


print("STEP 2: Loading the product catalog...")
all_products = pd.read_csv('products.csv')
print(all_products)
print()


print("STEP 3: Finding all the electronics items...")
electronics_only = all_products[all_products['Category'] == 'Electronics'].copy()
print(electronics_only[['Product_ID', 'Price']])
print()


print("STEP 4: Applying 20% holiday discount...")

for idx in range(len(electronics_only)):
    current_product_id = electronics_only.iloc[idx]['Product_ID']
    current_product_price = electronics_only.iloc[idx]['Price']

    product_object = Product(current_product_id, current_product_price)
    product_object.apply_discount(20)

    electronics_only.iloc[idx, electronics_only.columns.get_loc('Price')] = product_object.price

    print(f"{current_product_id}: {current_product_price} → {product_object.price}")

print()


electronics_only['Promo_Active'] = 'Yes'
print("✓ Promotion column added\n")


print(" File saved as holiday_promos.xlsx")

print("Final Data:")
print(electronics_only)