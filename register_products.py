from main import Product

try:
    product_price = input("Enter price \n")
    product_quantity = input("Enter quantity \n")
    product_description = input("Type product description \n")
    product_color = input("Enter color of product \n")

    Product.create(prod_price=product_price, prod_quantity=product_quantity, prod_description=product_description, color=product_color)
    print("Product Saved Successfully")
except:
    print("Failed to Save Product")