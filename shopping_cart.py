def add_to_cart(cart):
    item = input("What would you like to add ? ").lower()
    if item in cart:
        amount = int(input("How many of this item would you like to add ? "))
        cart[item]['amount'] += amount
    else:
        price = int(input("What is the price of your item ? "))
        amount = int(input("How many of this would you like to add ? "))
        cart[item]['price': price, 'amount': amount]


def view_cart(cart):
    total_price = 0
    if not  cart:
        print("You don't have anything in your cart")
    else:
        for key,value in cart:
            print(f"Here is your current cart {key['amount']} {'item'} ${value['price']}")
        total_price += key['amount'] * value['price']
        print(f"Here is your total {total_price}$")


def remove(cart):
    if not cart:
        print("You don't have anything in your cart.")
    else:
        view_cart(cart)
        item = input("What would you like to remove from your cart").lower()
        if item not in cart:
            print(f"{item} is not in your cart")
        else:
            ra = int(input("How many of this item would you like to remove"))   #ra stands for remove amount
            if ra == 'remove all':
                del cart[item]
            else:
                cart['amount'] -= ra



def go_to_checkout(cart):
    if not cart:
        print("You don't have anything in your cart")
    else:
        print("Here is your reciept")
        view_cart(cart)
        cr_option = input("Would you like to pay in cash or card ? ").lower()
        if cr_option == 'Card':
            print("please insert your credit card here.")
        elif cr_option == 'Cash':
            print("please insert cash here and change here.")


def main():
    print("Hello welcome to Omar's store.")
    cart = {}
    while True:
        options = input("Please select one of the following Add / Remove / View Cart / Go to checkput ").lower()
        if options == 'go to checkout':
            go_to_checkout(cart)
            break
        elif options == 'add':
            add_to_cart(cart)
        elif options == 'remove':
            remove(cart)
        elif options == 'view cart':
            view_cart(cart)
        else:
            print("Invalid choice")
    print("Thanks for shopping with us we hope to see you again.")

main()
