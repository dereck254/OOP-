from main import Product

products = Product.select()
for product in products:
    print(product.prod_price, product.prod_quantity, product.prod_description, product.color)