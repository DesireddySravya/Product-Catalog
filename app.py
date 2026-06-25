from flask import Flask, render_template
import csv

app = Flask(__name__)

PRODUCTS_CSV = 'products.csv'


def load_products(csv_path):
    products = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['price'] = float(row['price']) if row.get('price') else 0.0
            products.append(row)
    return products


@app.route('/')
def product_catalog():
    products = load_products(PRODUCTS_CSV)
    return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
