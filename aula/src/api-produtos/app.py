from fastapi import FastAPI
from models.product import Product

app = FastAPI()

@app.get('/api/name/{name}')
def get_hello(name: str):
    if not name:
        pass
    return {'Hello': name}


dataProducts = [
    Product(id=1, name='Airpods', description='Fone de Ouvido Apple', price=1300.99),
    Product(id=2, name='Instamax', description='Fotografia', price=500.99),
    Product(id=2, name='Iphone 15', description='Apple', price=15000.00),
]

@app.get('/api/products')
def get_products():
    return dataProducts