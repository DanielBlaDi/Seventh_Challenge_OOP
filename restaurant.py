class MenuItem:
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.__name: str = name
        self.__price: float = price  
        self.__quantity: int = quantity

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, new_name) -> None:
        if new_name:
            self.__name = new_name

    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, new_price) -> None:
        if new_price:
            self.__price = new_price

    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @quantity.setter
    def quantity(self, new_quantity)-> None:
        if new_quantity:
            self.__quantity = new_quantity

    def __str__(self):
        return f"Food: {self.__name}, price {self.__price}, quantity {self.__quantity}"

    def add_quantity(self, new_quantity: float)-> None:
        if new_quantity < 0:
            raise ValueError("You can't order a quantity of food =< 0 ")
        self.quantity += new_quantity


    def subtract_quantity(self, new_quantity : float)-> None:
        if new_quantity > self.quantity:
            raise ValueError("You can't order a quantity of food < 0 ")
        self.quantity -= new_quantity
    

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, alcohol: bool, quantity: int = 0):
        super().__init__(name, price, quantity)
        self.__alcohol: bool = alcohol
    
    def get_alcohol(self):
        return self.__alcohol
    
    def set_alcohol(self, new_alcohol):
        if new_alcohol:
            self.__alcohol = new_alcohol


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, origin: str, quantity: int = 0):
        super().__init__(name, price, quantity)
        self.__origin:str = origin
        
    def get_origin(self):
        return self.__origin
    
    def set_origin(self, new_origin):
        if new_origin:
            self.__origin = new_origin

    

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, vegan: bool, quantity: int = 0):
        super().__init__(name, price, quantity)
        self.__vegan: bool = vegan
    
    def get_vegan(self):
        return self.__vegan
    
    def set_vegan(self, new_vegan):
        if new_vegan:
            self.__vegan = new_vegan



class Dessert(MenuItem):
    def __init__(self, name: str, price: float, kind: str, quantity: int = 0):
        super().__init__(name, price, quantity)
        self.__kind:str = kind
        
    def get_kind(self):
        return self.__kind
    
    def set_kind(self, new_kind):
        if new_kind:
            self.__kind = new_kind



class Order:
    def __init__(self, Menu_items: "RegisterOrder"):
        self.__Menu_items: "RegisterOrder" = Menu_items
        self.__total_bill: float = 0

    @property
    def total_bill(self):
        return self.__total_bill
    
    @total_bill.setter
    def total_bill(self, new_bill):
        if new_bill:
            self.__total_bill = new_bill
    

    def add_items(self, new_food: MenuItem, new_food_quantity: float):
        if not isinstance(new_food, MenuItem):
            raise TypeError("You should order a MenuItem")
        new_food: MenuItem = new_food
        if new_food in self.__Menu_items:
            item_index: int = self.__Menu_items.order_item_index(new_food)
            self.__Menu_items[item_index].add_quantity(new_food_quantity)
        else:
            self.__Menu_items.add_item(new_food)


    def remove_items(self, new_food: MenuItem, new_food_quantity: float):
        if not isinstance(new_food, MenuItem):
            raise TypeError("You should order a MenuItem")
        new_food: MenuItem = new_food
        if new_food in self.__Menu_items:
            item_index: int = self.__Menu_items.order_item_index(new_food)
            self.__Menu_items[item_index].subtract_quantity(new_food_quantity)
        else:
            raise ValueError(f"You have not order {new_food}, how could you remove this from your order?")




    def calculate_total_bill(self):
        total_money = []
        for i in self.__Menu_items:
            total_money.append(i.get_price())
        return sum(total_money)


    def calculate_discounts(self):
        total_discount = self.calculate_total_bill()
        total_price = self.calculate_total_bill()
        
        has_appetizer = any(isinstance(item, Appetizer) for item in self.__Menu_items)

        has_dessert = any(isinstance(item, Dessert) for item in self.__Menu_items)

        has_beverage = any(isinstance(item, Beverage) for item in self.__Menu_items)

        if has_appetizer:
            total_discount = (total_discount - total_price*0.025)
        
        if has_dessert:
            total_discount = (total_discount - total_price*0.05)

        if has_beverage:
            total_discount = (total_discount - total_price*0.035)
        
        return(round(total_discount, 2))
    


    def __str__(self):
        print("Order:")
        for food in self.__Menu_items:
            yield f"food: {food.name}, price: {food.price}, quantity: {food.quantity}"

        print(self.__total_bill)





class RegisterOrder:
    def __init__(self) -> None:
        self.menu_items = []

    def add_item(self, item: MenuItem) -> None:
        self.menu_items.append(item)

    def order_item_index(self, item):
        self.menu_items.index(item)

    def remove_item(self, item: MenuItem) -> None:
        self.menu_items.remove(item)

    def __iter__(self):
        return RegisterOrderIterator(self.menu_items)


class RegisterOrderIterator:
    def __init__(self, menu_items: Order) -> None:
        self.menu_items = menu_items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.menu_items):
            item = self.menu_items[self.index]
            return item
        else:
            raise StopIteration
        


class Payment_method:
  def __init__(self):
    pass

  def pagar(self, money):
    raise NotImplementedError()

class Credit_card(Payment_method):
  def __init__(self, number, cvv):
    super().__init__()
    self.number = number
    self.cvv = cvv

  def pagar(self, money):

    print(f"Paying {money} with credit card {self.number[-4:]}")

class Cash(Payment_method):
  def __init__(self, money_payed):
    super().__init__()
    self.money_payed = money_payed

  def pagar(self, money):

    if self.money_payed >= money:
      print(f"Sucessfully payment. Exchange: {self.money_payed - money}")
    else:
      print(f"Sorry, you will have to wash the dishes. Missing {money - self.money_payed} for completing the payment .")


if __name__ == "__main__":
    

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




    Menu = {"lemonade":lemonade, "water":water, "beer":beer, "empanada":empanada, "arepa":arepa, "chinese rise":chinese_rise, "hamburger":hamburger, "vegan hamburger":vegan_hamburger, "orange ice cream":ice_cream, "Banana Cake":cake, "sweet mind":candys}



    print("Menu")
    print("lemonade, water, beer, empanada, arepa, chinese rise, hamburger, vegan hamburger, Banana Cake, sweet mind, orange ice cream")

    print("So, you want a cake, a empanada, a water and a hamburger")

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


    start_pay: bool = True
    attems: int  = 0
    while finish_pay or start_pay:
        finish_pay: bool = True
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
                    pay_credit_card = Credit_card(number=credit_card, cvv=cvv)
                    pay_credit_card.pagar(First_order.calculate_discounts())
                    finish_pay: bool = False
                    
            case "efective":
                money_have: int = int(input("How much money do you have?:\n"))
                pay_efective = Cash(money_payed=money_have)
                pay_efective.pagar(First_order.calculate_discounts())
                finish_pay: bool = False
            case _:
                print("Invalid payment method")
        
        attems += 1
        if attems == 5:
            print("I will call the police")
        