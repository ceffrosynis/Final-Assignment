import pandas as pd
import numpy as np
from matplotlib.colors import to_rgba
from matplotlib import pyplot as plt

filename = 'filename.csv'

csv_table = pd.read_csv(filename)

total_bottles_sold_per_zip_item = csv_table.groupby([ 'zip_code', 'item_description' ])[ 'bottles_sold' ].sum().reset_index()
plt.subplot(2, 1, 1)
for item in total_bottles_sold_per_zip_item[ 'item_description' ].unique():
    item_rows = total_bottles_sold_per_zip_item[ total_bottles_sold_per_zip_item[ 'item_description' ] == item ]
    plt.scatter(item_rows[ 'zip_code' ], item_rows[ 'bottles_sold' ])
plt.title("Items sold based on zip code")
plt.xlabel("zio code")
plt.ylabel("Total sales")

total_bottles_sold_per_store = csv_table.groupby([ 'store_name' ])[ 'bottles_sold' ].sum()
total_sells = total_bottles_sold_per_store.sum()

sales_percentage_per_store = total_bottles_sold_per_store / total_sells * 100
max_sales_percentage_per_store = sales_percentage_per_store.max()
sales_percentage_per_store.sort_values(ascending=True, inplace=True)

sales_percentage_per_store = sales_percentage_per_store.tail(10)

plt.subplot(2, 1, 2)
plt.barh(sales_percentage_per_store.index, sales_percentage_per_store, color=[to_rgba('darkred', alpha=perc / max_sales_percentage_per_store) for perc in sales_percentage_per_store])
plt.title("Percentage of sales per store")
plt.xlabel("Percentage of sales")
plt.ylabel("Store")
plt.show()
