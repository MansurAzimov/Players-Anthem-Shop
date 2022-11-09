from shop import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template ('contact.html')

@app.route('/signup')
def signup():
    return render_template ('signup.html')

@app.route('/register')
def register():
    return render_template ('register.html')

@app.route('/checkout')
def checkout():
    return render_template ('checkout.html')

@app.route('/products')
def products():
    return render_template ('products.html')