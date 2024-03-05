cart = {}
total_price = 0

def adding_price():
    price*price


def add_to_cart(product, price, amount):
    if product not in cart:
        print("How many of this product woul you like to add? ")
        cart[product]= {'price':price, 'quantity':amount}
    else:
        cart[product]['quantity'] += amount
    return cart


def remove(product):
    if product in cart:
        del cart[product]
        print('You have removed this product from your cart')

def list_cart():
    if not cart:
        print("Your cart is empty")
    else:
        print(f"Here is your current {cart}")


def main():
    print("Hello welcome to omar's store")
    options = input("what would you like to do today choose one of the following Add/Remove/list cart/quit").lower()
    if options == "add":
        product = input("What would you like to add to your cart? ")
        price = input("How much does it cost?")
        amount = input("Excellent, how many of this item would you like to add? ")
        cart = add_to_cart(product,price,amount)
    elif main == 'remove':
        product = input("what would you like to remove? ")
        remove(product)
    elif options == 'list':
        list_cart()
    elif options == 'quit':
        print(f"Thank you for shopping with us here is your current{cart}")
            

main()