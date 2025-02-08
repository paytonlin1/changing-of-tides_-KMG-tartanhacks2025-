from flask import Flask, render_template
from waitress import serve
import random
# import pandas as pd
import csv
app = Flask(__name__)

images = []
product_names = []
descriptions = []
prices = []
ratings = []
retailers = []
links = []
with open('tide.csv', mode ='r')as file:
    csvfile = csv.reader(file)
    for lines in csvfile:
        images.append(lines[6])
        prices.append(lines[2])
        product_names.append(lines[0])
        descriptions.append(lines[4])
        retailers.append(lines[3])
        links.append(lines[5])


@app.route('/')
@app.route('/main')
def hello_world():
    return render_template('main.html')

@app.route('/nextproduct')
def next_product():
    rand_product = random.randint(0,31)
    return render_template('product.html', price=prices[rand_product], image=images[rand_product], description=descriptions[rand_product], retailer=retailers[rand_product], name=product_names[rand_product], link=links[rand_product])

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
