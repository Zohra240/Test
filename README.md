# Scraping jvbazar Website - Using BeautifulSoup
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

products = []   # List to store names of the products
prices = []     # List to store prices of the products

sp = requests.get("https://jvbazar.com/shop/")
sp = BeautifulSoup(sp.content, 'html.parser')

for each in sp.find_all('div',  attrs={'class':'box-text box-text-products'}):
    # name = each.find('a', href=True, attrs={'class':'woocommerce-LoopProduct-link woocommerce-loop-product__link'})
    # price = each.find('span', attrs={'class':'woocommerce-Price-currencySymbol'})
    name = each.find('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link').text.strip()
    price = each.find('span', class_='woocommerce-Price-amount amount').text.strip()

    if name is None:    # Caters for instances where the name does not exist
        products.append(None)
    else:
        products.append(name) # Get the text part

    if price is None:
        prices.append(None)
    else:
        prices.append(price)

# Structuring and storing data
df = pd.DataFrame({'Product_Name': products, 'Price': prices}) 
print(df.to_string())

# Output the DataFrame to CSV file
df.to_csv('products.csv', index = False)

# Data Visualization
df2 = pd.read_csv("products.csv")

plt.xlabel("Product_Name")
plt.ylabel("Price")
plt.title("Product against Price")

plt.scatter(df2.Product_Name, df2.Price, marker="*", c = 'purple', alpha = 1)    # Line graph - The labels above apply for this plot only
# marker: format can be o or * , c: color, alpha: opacity(Range: 0-1)
plt.show()
