import pandas as pd
sales_data = {
    "Product A": 100,
    "Product B": 80,
    "Product C": 120,
    "Product D": 150,
    "Product E": 90,
    "Product F": 60,
}
df = pd.DataFrame(list(sales_data.items()), columns=["Product", "Quantity Sold"])
df_sorted = df.sort_values(by="Quantity Sold", ascending=False)
top_5_products = df_sorted.head(5)
print("Top 5 products sold the most in the past month:")
print(top_5_products)
