
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/size', methods=['POST'])
def select_size():
    if request.method == 'POST':
        product_size = request.form['size']

    adidas.provide_size(product_size)

    return product_size
