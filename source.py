from flask import Flask, render_template
from waitress import serve
import random
import pandas as pd

app = Flask(__name__)
image = []
product_name = []
description = []
price = []
rating = []
df = pd.read_csv('tide.csv')
# print(df.dtypes)

#---------------------------------------------------------------Images
df_image = df['Image']

for i in range(len(df_image)):
    image.append(df_image[i])
#---------------------------------------------------------------ProductName
df_product_name = df['Product Name']

for i in range(len(df_product_name)):
    product_name.append(df_product_name[i])
#---------------------------------------------------------------Description
df_description = df['Description']

for i in range(len(df_description)):
    description.append(df_description[i])
#---------------------------------------------------------------Price
df_price = df['Cost']

for i in range(len(df_price)):
    price.append(df_price[i])
#---------------------------------------------------------------Rating
df_rating = df['Rating']

for i in range(len(df_rating)):
    rating.append(df_rating[i])
#---------------------------------------------------------------All-For-Loops

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/nextproduct')
def next_product():
    rand_product = random.randint(0,2)
    return render_template('product.html', price=prices[rand_product], image=images[rand_product])

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
