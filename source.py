from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/nextproduct')
def next_product():
    return render_template('product.html', price=8.99, image="https://images.ctfassets.net/ajjw8wywicb3/1gXSuHYRnGI3SJX8SBbN1l/f04f1c1f600fe4ae4f2e80b01bb41337/Tide_Oxi_Boost_Power_Pods_EN-US_hero_SP_748x748.png?fm=png")

if __name__ == '__main__':
    app.run()
