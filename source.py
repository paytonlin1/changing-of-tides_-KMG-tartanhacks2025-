from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/nextproduct')
def next_product():
    return render_template('product.html')

if __name__ == '__main__':
    app.run()
