from django.db import migrations
from main.models import Product

def create_test_products(apps, schema_editor):
    Product = apps.get_model('main', 'Product')
    test_products = [
        {'name': 'Product 1', 'description': 'Description for product 1', 'price': 10.99, 'stock': 100},
        {'name': 'Product 2', 'description': 'Description for product 2', 'price': 20.99, 'stock': 200},
        {'name': 'Product 3', 'description': 'Description for product 3', 'price': 30.99, 'stock': 300},
        {'name': 'Product 4', 'description': 'Description for product 4', 'price': 40.99, 'stock': 400},
        {'name': 'Product 5', 'description': 'Description for product 5', 'price': 50.99, 'stock': 500},
        {'name': 'Product 6', 'description': 'Description for product 6', 'price': 60.99, 'stock': 600},
        {'name': 'Product 7', 'description': 'Description for product 7', 'price': 70.99, 'stock': 700},
        {'name': 'Product 8', 'description': 'Description for product 8', 'price': 80.99, 'stock': 800},
        {'name': 'Product 9', 'description': 'Description for product 9', 'price': 90.99, 'stock': 900},
        {'name': 'Product 10', 'description': 'Description for product 10', 'price': 100.99, 'stock': 1000},
    ]
    for data in test_products:
        Product.objects.create(**data)

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_test_products),
    ]