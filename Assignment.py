# Scraping jvbazar Website - Using BeautifulSoup
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

products = []   # List to store names of the products
prices = []     # List to store prices of the products

sp = requests.get("https://jvbazar.com/shop/")
sp = BeautifulSoup(sp.content, 'html.parser')

for each in sp.find_all('p',  attrs={'class':'name product-title woocommerce-loop-product__title'}):
    name = each.find('a', href=True, attrs={'class':'woocommerce-LoopProduct-link woocommerce-loop-product__link'})
    price = each.find('span', attrs={'class':'woocommerce-Price-currencySymbol'})
     
 
    if name is None:    # Caters for instances where the name does not exist
        products.append(None)
    else:
        products.append(name.text) # Get the text part

 

text = "nbsp$: 750 nb"

# Remove unwanted characters using strip
price = text.strip('nbsp$: nb')

# Check if the stripped text is numeric
if price.isdigit():
    prices = price
else:
    prices = None

print(f"The extracted price is: {prices}")

# Structuring and storing data
df = pd.DataFrame({'Product_Name': products, 'Price': prices}) 
print(df.to_string())

# Output the DataFrame to CSV file
df.to_csv('products.csv', index = False)

# Data Visualization
df2 = pd.read_csv("products.csv")

plt.xlabel("Product_Name")
plt.ylabel("Price")
plt.title("Rating against Price")

plt.scatter(df2.Product_Name, df2.Price, marker="*", c = 'red', alpha = 1)    # Line graph - The labels above apply for this plot only
# marker: format can be o or * , c: color, alpha: opacity(Range: 0-1)
plt.show()
