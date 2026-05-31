def show_cart():
    cart = [100, 250, 75]

    if len(cart) == 0:
        return "Cart is empty"

    return cart

print("Shopping Cart:", show_cart())