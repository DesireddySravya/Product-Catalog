# Product Catalog

A complete Flask-based product catalog website with searchable products, category filtering, and individual product detail pages.

## Features

- Browse products by category
- Search products by name, description, or category
- Product detail page for each item
- REST API endpoint at `/api/products`
- Responsive layout with modern styling

## Setup

1. Create and activate a Python virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the application:

```powershell
python app.py
```

4. Open the site in your browser:

`http://127.0.0.1:5000`

## Files

- `app.py` — Flask application and request handlers
- `products.json` — product catalog data source
- `templates/` — HTML templates for pages
- `static/css/styles.css` — site styling

## API

- `GET /api/products` — returns the full product list as JSON
