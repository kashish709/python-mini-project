from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Sample product data
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.99},
    {'id': 2, 'name': 'Product 2', 'price': 12.99},
    {'id': 3, 'name': 'Product 3', 'price': 15.99},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product)
    session.modified = True  # Mark session as modified
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total_price = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart=cart_items, total_price=total_price)

@app.route('/checkout')
def checkout():
    session.pop('cart', None)  # Clear the cart after checkout
    return "Thank you for your purchase!"

if __name__ == '__main__':
    app.run(debug=True)
