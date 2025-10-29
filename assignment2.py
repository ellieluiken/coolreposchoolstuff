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
    cursed_antiques.sort()
    for i, name in enumerate(cursed_antiques, start=1):
        print(f'Item {i}: {name}')
     


while True:

    user_input = input("What do you want to do (buy/list/cart/remove/quit)? ").casefold()
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
                        if add_input in cursed_antiques:
                            shopping_cart.append(add_input)
                            cursed_antiques.remove(add_input)
                            print(f'{add_input} has been added to the shopping cart!')
                        elif add_input in shopping_cart:
                            print("Item is already in the shopping cart. Please try again.")

                    except ValueError:
                            print("That item does not exist. Please try again.")
                    

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
              shopping_cart.sort()
              for i, name in enumerate(shopping_cart, start=1):
                    print(f'Item {i}: {name}')

        case 'sort':
              cursed_antiques.sort()


        case _:
              print("Error, please try again")
