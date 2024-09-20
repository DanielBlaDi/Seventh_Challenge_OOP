from restaurant import *


if __name__ == "__main__":
    

    lemonade = Beverage(name="Lemonade", price=2000, alcohol=False)
    beer = Beverage(name="Beer", price=3000, alcohol=False)
    water = Beverage(name="Water", price=1000, alcohol=False)


    empanada = Appetizer(name="Lemonade", price=1500, origin="Colombia")
    arepa = Appetizer(name="Lemonade", price=2200, origin="Venezuela")
    


    chinese_rise = MainCourse(name="Chinese rise", price=20000, vegan=False)
    hamburger = MainCourse(name="Hamburger", price=25000, vegan=False)
    vegan_hamburger = MainCourse(name="Vegan_hambuerger", price=30000, vegan=True)



    ice_cream = Dessert(name="orange ice cream", price=3000, kind="Ice Cream")
    candys = Dessert(name="sweet mind", price=500, kind="Candy")
    cake = Dessert(name="Banana Cake", price=4500, kind="Cake")

    print("Menu")
    print("lemonade, water, beer, empanada, arepa, chinese rise, hamburger, vegan hamburger, Banana Cake, sweet mind, orange ice cream\n")

    print("So, you want a cake, a empanada, a water and a hamburger\n")

    First_order: Order = Order([cake, empanada, water, hamburger])

    start = True
    new_food = []
    while start or mores_food:
        start = False
        more_food: str = input("Would you like more food, yes or no?\n" )
        if more_food == "yes":
            mores_food = True
            food = input("Which one?: ")
            match food:
                case "lemonade": 
                    wished_food = lemonade
                case "beer":
                    wished_food = beer
                case "water":
                    wished_food= water
                case "arepa": 
                    wished_food = arepa
                case "empanada":
                    wished_food = empanada
                case "chinise rise":
                    wished_food= chinese_rise
                case "hamburger": 
                    wished_food = hamburger
                case "vegan hamburger":
                    wished_food = vegan_hamburger
                case "orange ice cream":
                    wished_food= ice_cream
                case "Banana Cake":
                    wished_food = cake
                case "sweet mind":
                    wished_food= candys
            new_food.append(wished_food)
        else:
            mores_food = False
        

    First_order.add_items(new_food=new_food)
        
    print("Your bill without discount is: ",First_order.calculate_total_bill())
    print("your bill with discounts is: ", First_order.calculate_discounts())


        
    print("This will be the two methods on payment: ")
    payment = input("Enter credit card or efective:\n")
    match payment:
        case "credit card":
            fuc: bool = True
            credit_card: str = input("Enter your credit card number:\n")
            cvv: str = input("Enter the password:\n")
            if len(credit_card) != 13:
                print("This is not the number of a credit card")
                fuc: bool = False
            if len(cvv) != 3:
                print("This is not the cvv")
                fuc: bool = False
            if fuc:
                cvv: int = int(cvv)
                pay1 = Credit_card(number=credit_card, cvv=cvv)
                pay1.pagar(First_order.calculate_discounts())
                
        case "efective":
            money_have: int = int(input("How much money do you have?:\n"))
            pay1 = Cash(money_payed=money_have)
            pay1.pagar(First_order.calculate_discounts())

        case _:
            print("Invalid payment method")
    