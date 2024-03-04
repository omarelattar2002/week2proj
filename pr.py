products = ['Milk', 'Eggs', 'Salmon', 'Yogurt', 'Butter', 'Chips']



def add():



def shopping_cart():
    cart = []
    while True:
        choice = input("Hello, What would you like to do with your cart please? select one of the following Add/Remove/Go to Checkout ").lower()
        if choice == 'Go to Checkout'.lower():
            break
        elif choice == 'Add'.lower():
            add = input(f'What would you like to add from{products}? ')
            
            if add == 'Milk'.lower():
                print(cart.append('Milk'.lower()))
            print(cart)
            additional_choice = input("Would you like to add anything else")
            if additional_choice == 'add more items':
                more_items = input('What would you like to add')
                shopping_cart[more_items]

#I still haven't finished I feel like there is a lot of confusion regarding functions I am going to do more work on it still


shopping_cart()
