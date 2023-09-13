# Scraping Shopify Website - Using BeautifulSoup
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

products = []   # List to store names of the products
prices = []     # List to store prices of the products
ratings = []    # List to store ratings of the products

sp = requests.get("https://admin.shopify.com/store/f3d03f-2/products,b5g&marketplace=SHOPIFY")
sp = BeautifulSoup(sp.content, 'html.parser')

for each in sp.find_all('a', href=True, attrs={'class':'_1fQZEK'}):
    name = each.find('div', attrs={'class':'_4rR01T'})
    price = each.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rate = each.find('div', attrs={'class':'_3LWZlK'})

    if name is None:    # Caters for instances where the name does not exist
        products.append(None)
    else:
        products.append(name.text) # Get the text part

    if price is None:
        prices.append(None)
    else:
        prices.append(price.text)

    if rate is None:    # Caters for instances where the rating does not exist - which was causing an error initially
        ratings.append(None)
    else:
        ratings.append(rate.text)

# Structuring and storing data
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings}) 
print(df.to_string())

# Output the DataFrame to CSV file
df.to_csv('products.csv', index = False)

# Data Visualization
df2 = pd.read_csv("products.csv")

plt.xlabel("Rating")
plt.ylabel("Price")
plt.title("Rating against Price")

plt.scatter(df2.Rating, df2.Price, marker="*", c = 'red', alpha = 1)    # Line graph - The labels above apply for this plot only
# marker: format can be o or * , c: color, alpha: opacity(Range: 0-1)
plt.show()
