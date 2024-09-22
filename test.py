from restaurant import*

def show_menu(menu):
    print("Menu:\n")
    for x in menu:
        print(menu[x])
    print()


lemonade = Beverage(name="Lemonade", price=2000, alcohol=False)
beer = Beverage(name="Beer", price=3000, alcohol=False)
water = Beverage(name="Water", price=1000, alcohol=False)


empanada = Appetizer(name="Empanada", price=1500, origin="Colombia")
arepa = Appetizer(name="Arepa", price=2200, origin="Venezuela")



chinese_rise = MainCourse(name="Chinese rise", price=20000, vegan=False)
hamburger = MainCourse(name="Hamburger", price=25000, vegan=False)
vegan_hamburger = MainCourse(name="Vegan hambuerger", price=30000, vegan=True)



ice_cream = Dessert(name="Orange ice cream", price=3000, kind="Ice Cream")
candys = Dessert(name="Sweet mind", price=500, kind="Candy")
cake = Dessert(name="Banana Cake", price=4500, kind="Cake")


menu = {"lemonade":lemonade, "water":water, "beer":beer, "empanada":empanada, "arepa":arepa, 
    "chinese rise":chinese_rise, "hamburger":hamburger, "vegan hamburger":vegan_hamburger, 
    "orange ice cream":ice_cream, "Banana Cake":cake, "sweet mind":candys}


register: RegisterOrder = RegisterOrder()
first_order: Order = Order(register)

print("So, what would you like? We have:")
show_menu(menu)



start_order: bool = True
while start_order:
    try:
        if len(register) > 0:
            remove_food: str = input("\nWould you like to remove some food from your order?, yes or no\n" )
            if remove_food == "yes":
                print(first_order)
                removed_food: str = input("Which one?: (only one, without capital letters)\n")
                quantity_removed_food: int = int(input("How much?: (int numbers)\n"))
                if removed_food not in register:
                    raise ValueError("You should write a food of our menu for your order \n")
                wished_removed_food: MenuItem = menu[removed_food]
                first_order.remove_items(new_food=wished_removed_food, new_food_quantity=quantity_removed_food)

                print(f"You have remove a quantity of {quantity_removed_food} {remove_food} from your order\n")

                print(first_order)
                print()



        more_food: str = input("\nWould you like to add more food to your order?, yes or no\n" )
        if more_food == "yes":
            show_menu(menu)
            add_food: str = input("Which one?: (only one, without capital letters)\n")
            quantity_add_food: int = int(input("How much?: (int numbers)\n"))
            if add_food not in menu:
                raise ValueError("You should write a food of our menu for your order \n")
            wished_add_food: MenuItem = menu[add_food]
            first_order.add_items(new_food=wished_add_food, new_food_quantity=quantity_add_food)

            print(f"You have add a quantity of {quantity_add_food} of {add_food} to your order\n")
            print(first_order)
            print()



        order_ready: str = input("\nWould you like something more?, yes or no\n")
        if order_ready == "no":
            if len(register) != 0:
                start_order: bool = False
                tip: str = input("Would you like to give a tip?, yes or no\n")
                if tip == "yes":
                    first_order.calculate_total_bill(tip_bool = True)
                    total_bill: float =  first_order.total_bill
                    total_bill_bool: bool = True
                else:
                    first_order.calculate_total_bill()
                    total_bill: float =  first_order.total_bill
                    total_bill_bool: bool = True
            else:
                no_food: str = input("\nAre you sure you don't want some food?\n")
                if no_food == "yes":
                    start_order: bool = False
                    total_bill_bool: bool = False
        elif order_ready == "yes": 
            print(first_order)


    except Exception as e:
        print(e)

if total_bill_bool:
        start_pay: bool = True
        attems: int  = 0
        while start_pay:
            try:
                print("Your total bill is:",total_bill, end="\n")
                print("This will be the two methods on payment:\n")
                payment = input("Enter credit card or efective:\n")
                match payment:
                    case "credit card":
                        fuc: bool = True
                        credit_card: str = input("Enter your credit card number (without .):\n")
                        cvv: str = input("Enter the password:\n")
                        int(credit_card)
                        int(cvv)
                        if len(str(credit_card)) != 13:
                            print("This is not the number of a credit card\n")
                            fuc: bool = False
                        if len(str(cvv)) != 3:
                            print("This is not the cvv\n")
                            fuc: bool = False
                        if fuc:
                            pay_credit_card = Credit_card(number=credit_card, cvv=cvv)
                            pay_credit_card.pagar(total_bill)
                            start_pay: bool = False
                            
                    case "efective":
                            money_have: float = float(input("How much money do you have?:\n"))
                            pay_efective = Cash(money_payed=money_have)
                            pay_efective.pagar(total_bill)
                            start_pay: bool = False
                    case _:
                        print("Invalid payment payment\n")

            except Exception as e:
                print(e)

            attems += 1
            if attems == 5:
                print("I will call the police\n")

            if attems == 10:
                print("The police is here\n")
                start_pay: bool = False


