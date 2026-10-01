# Shop Product API

A simple Product API built with Django and Django REST Framework.
Anyone can view products; only authenticated users can add them.

## Installation

```bash
git clone https://github.com/Shuvonkar005/shop_api
cd shop_api
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
```

## Run migrations

```bash
python manage.py migrate
```

## Create a test user and token

```bash
python manage.py createsuperuser
python manage.py drf_create_token <username>
```

## Start the server

```bash
python manage.py runserver
```

## Endpoints

- `GET /api/products/` – list products (no token needed, 5 per page, use `?page=2`)
- `POST /api/products/` – add a product (requires header `Authorization: Token YOUR_TOKEN`)

## Screenshots

See the `screenshots/` folder.