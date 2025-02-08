from flask import Flask, render_template
from waitress import serve
import random
import pandas as pd
app = Flask(__name__)

# prices = [5.99, 6.99, 8.99]
# images = ["https://images.ctfassets.net/ajjw8wywicb3/1gXSuHYRnGI3SJX8SBbN1l/f04f1c1f600fe4ae4f2e80b01bb41337/Tide_Oxi_Boost_Power_Pods_EN-US_hero_SP_748x748.png?fm=png", "https://images.ctfassets.net/ajjw8wywicb3/5mXim6zecmNQiIPaai2D0J/cfb6de903117a452a57cf5aa19c6c71b/50310_Tide_Belize_Original_hero_SP_748x748.jpg?fm=png", "https://images.ctfassets.net/ajjw8wywicb3/2gcpY5NwnDuauotkKJehv1/1567a41296d5105388cf27c0cb1cfcad/52339_TideBelize_BigPapa_HCHD_EN-US_hero_SP_748x748.jpg?fm=png"]

images = []
product_names = []
descriptions = []
prices = []
ratings = []
df = pd.read_csv('tide.csv')

#---------------------------------------------------------------Images
df_image = df['Image']

for i in range(len(df_image)):
    images.append(df_image[i])
#---------------------------------------------------------------ProductName
df_product_name = df['Product Name']

for i in range(len(df_product_name)):
    product_names.append(df_product_name[i])
#---------------------------------------------------------------Description
df_description = df['Description']

for i in range(len(df_description)):
    descriptions.append(df_description[i])
#---------------------------------------------------------------Price
df_price = df['Cost']

for i in range(len(df_price)):
    prices.append(df_price[i])
#---------------------------------------------------------------Rating
df_rating = df['Rating']

for i in range(len(df_rating)):
    ratings.append(df_rating[i])
#---------------------------------------------------------------All-For-Loops

@app.route('/')
@app.route('/main')
def hello_world():
    return render_template('main.html')

@app.route('/nextproduct')
def next_product():
    rand_product = random.randint(0,2)
    return render_template('product.html', price=prices[rand_product], image=images[rand_product])

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
