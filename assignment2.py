cursed_antiques = [
   
    "Talisman",
    "Monkeys Paw",
    "Cursed Mirror",
    "Haunted Painting",
    "Voodoo Doll",
    "Crystal Ball",
    "Cursed Locket",
    "Ancient Amulet",
    "Phantom Clock",
    "Dorian Gray's Portrait",
    "Cursed Ring"

]





shopping_cart = [
]


def display_list():
    for i, name in enumerate(cursed_antiques, start=1):
        print(f'Item {i}: {name}')
     
print("""Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - View cart (enter 'cart')
    - Quit (enter 'quit')""")

while True:
    
    user_input = input("What do you want to do? ").casefold()
    match user_input:
        
        case 'quit':
            break
        
        case 'buy':
                print("Available items are: ")
                display_list()
                            
                index_name_input = input("Would you like to purchase an item by name or index number? ")
                if index_name_input == 'index':
                    chosen_index_input = int(input("Please enter an index number: "))                     
                    try:  
                        chosen_antique = cursed_antiques[chosen_index_input]
                        shopping_cart.append(chosen_antique)
                        cursed_antiques.remove(chosen_antique)
                        print(f"{chosen_antique} has been added to your cart.")
                    except IndexError:
                         print("Value is out of range, please try again.")      
                
                elif index_name_input == 'name':
                
                    add_input = input("What item would you like to buy? ")

                    try:
                        if add_input not in shopping_cart:
                            shopping_cart.append(add_input)
                            cursed_antiques.remove(add_input)
                            print(f'{add_input} has been added to the shopping cart!')
                        elif add_input not in cursed_antiques:
                            print("Item is already in the shopping cart. Please try again.")

                    except ValueError:
                            print("That item does not exist. Please try again.")
                            shopping_cart.remove(add_input)
                    

        case 'remove':
                index_name_remove_input = input("Would you like to remove an item by name or index number? ")
                if index_name_remove_input == 'index':
                    try:
                        chosen_index_input = int(input("Please enter an index number: "))
                        if chosen_antique in shopping_cart:                  
                            shopping_cart.remove(chosen_antique)
                            cursed_antiques.append(chosen_antique)
                            print(f"{chosen_antique} has been removed from your cart.")
                    except IndexError:
                         print("Value is out of range, please try again.")
                
                elif index_name_remove_input == 'name':
                
                    remove_input = input("What would you like to remove from your shopping cart? ")
                    if remove_input in shopping_cart:
                        shopping_cart.remove(remove_input)
                        cursed_antiques.append(remove_input)
                        print(f'{remove_input} has been removed from your cart.')

                else:
                    print("Invalid input. Please try again.")
                   
        case 'list':
              display_list()

        case 'cart':
            print("Your shopping cart contains: ")
            for i, name in enumerate(shopping_cart, start=1):
                print(f'Item {i}: {name}')
              

        case 'sort':
            sort_input = input("Would you like to sort the antique list or the antiques in your cart? (list/cart): ").casefold()
            abc_input = input("Would you like to sort in alphabetical order or reverse alphabetical order? (a/z): ").casefold()
            match sort_input:
                case 'list':
                    match abc_input:
                        case 'z':
                            cursed_antiques.sort(reverse=True)
                            print("Antiques have been sorted in reverse alphabetical order.")
                        case 'a':
                            cursed_antiques.sort()
                            print("Antiques have been sorted in alphabetical order.")
                case 'cart':
                    match abc_input:
                        case 'z':
                            shopping_cart.sort(reverse=True)
                            print("Your cart has been sorted in reverse alphabetical order.")
                        case 'a':
                            shopping_cart.sort()
                            print("Your cart has been sorted in alphabetical order.")
                              
                           


        case _:
              print("Error, please try again")
