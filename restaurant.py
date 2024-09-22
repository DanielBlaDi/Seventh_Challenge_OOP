class MenuItem:
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.__name: str = name
        self.__price: float = price  
        self.__quantity: int = quantity

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, new_name: str) -> None:
        if new_name:
            self.__name = new_name

    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, new_price: float) -> None:
        if new_price:
            self.__price = new_price

    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        if new_quantity < 0 and isinstance(new_quantity, int):
            raise ValueError("Quantity cannot be negative")
        self.__quantity = new_quantity

    def __str__(self):
        return f"Food: {self.__name}, price : {self.__price}"

    def add_quantity(self, new_quantity: float)-> None:
        self.quantity += new_quantity


    def subtract_quantity(self, new_quantity : float)-> None:
        if new_quantity > self.quantity:
            raise ValueError("You can't order a quantity of food < 0")
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
        self.__tip: float = 0
        self.__discounts:str = 0
        self.__total_bill: float = 0
    @property
    def total_bill(self) -> float:
        return self.__total_bill
    
    @total_bill.setter
    def total_bill(self, new_bill):
        if new_bill:
            self.__total_bill = new_bill


    @property
    def tip(self) -> float:
        return self.__tip
    
    @tip.setter
    def tip(self, new_tip):
        if new_tip:
            self.__tip = new_tip

    @property
    def discounts(self) -> float:
        return self.__discounts
    
    @discounts.setter
    def discounts(self, new_discounts):
        if new_discounts:
            self.__discounts = new_discounts
    
    def add_items(self, new_food: MenuItem, new_food_quantity: float) -> None:
        if not isinstance(new_food, MenuItem):
            raise TypeError("You should order a MenuItem")
        if new_food in self.__Menu_items:
            item_index: int = self.__Menu_items.order_item_index(new_food)
            self.__Menu_items[item_index].add_quantity(new_food_quantity)
        else:
            new_food.add_quantity(new_quantity=new_food_quantity)
            self.__Menu_items.add_item(new_food)
            

    def remove_items(self, new_food: MenuItem, new_food_quantity: float) -> None:
        if not isinstance(new_food, MenuItem):
            raise TypeError("You should order a MenuItem")
        new_food: MenuItem = new_food
        if new_food in self.__Menu_items:
            item_index: int = self.__Menu_items.order_item_index(new_food)
            self.__Menu_items[item_index].subtract_quantity(new_food_quantity)
            if new_food.quantity == 0:
                self.__Menu_items.remove_item(new_food)

        else:
            raise ValueError(f"You have not order {new_food}, how could you remove this from your order?")


    def calculate_total_cost(self) -> float:
        total_money: int = 0
        for item in self.__Menu_items:
            total_money += (item.price *item.quantity)
        return total_money


    def calculate_discounts(self) -> float:
        total_discount = self.calculate_total_cost()
        total_price = self.calculate_total_cost()

        has_appetizer = any(isinstance(item, Appetizer) for item in self.__Menu_items)

        has_dessert = any(isinstance(item, Dessert) for item in self.__Menu_items)

        has_beverage = any(isinstance(item, Beverage) for item in self.__Menu_items)


        if has_appetizer:
            total_discount = (total_discount - total_price*0.025)
            self.discounts += total_price*0.025

        if has_dessert:
            total_discount = (total_discount - total_price*0.05)
            self.discounts += total_price*0.05

        if has_beverage:
            total_discount = (total_discount - total_price*0.035)
            self.discounts += total_price*0.035

        return (round(total_discount, 2))
    

    def apply_tip(self, tip_bool: bool = False) -> None:
        total: float = self.calculate_discounts()
        if tip_bool:
            self.tip: float = (total*10)/100
        else:
            self.tip: float = 0
        

    def calculate_total_bill(self, tip_bool: bool = False) -> None:
        total: float = self.calculate_discounts()
        self.apply_tip(tip_bool)
        total_bill:float = total + self.tip
        self.total_bill = total_bill



    def generate_order_details_food(self):
        for food in self.__Menu_items:
            yield f"food: {food.name}, price: {food.price}, quantity: {food.quantity}, total: {food.quantity*food.price}"

    def __str__(self):
        self.calculate_total_bill()
        if len(self.__Menu_items) == 0:
            return "You have not order anything"
        else:
            order_details = "Order:\n"
            for food in self.generate_order_details_food():
                order_details += food + "\n"
            
            if self.discounts != 0:
                order_details += f"Discount: {self.discounts}\n"


            if self.tip != 0:
                            order_details += f"Tip of 10%: {self.tip}\n"
            order_details += f"Total bill: {self.total_bill}\n"
            return order_details




class RegisterOrder:
    def __init__(self) -> None:
        self.menu_items = []

    def add_item(self, item: MenuItem) -> None:
        self.menu_items.append(item)

    def order_item_index(self, item):
        return self.menu_items.index(item)

    def remove_item(self, item: MenuItem) -> None:
        self.menu_items.remove(item)

    def __getitem__(self, index: int) -> MenuItem:
        return self.menu_items[index]

    def __len__(self) -> int:
        return len(self.menu_items)

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
            self.index += 1
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
    self.number: str = number
    self.cvv: str = cvv

  def pagar(self, money) -> None:

    print(f"Paying {money} with credit card {self.number[-4:]}")

class Cash(Payment_method):
  def __init__(self, money_payed):
    super().__init__()
    self.money_payed: float = money_payed

  def pagar(self, money) -> None:

    if self.money_payed >= money:
      print(f"Sucessfully payment. Exchange: {self.money_payed - money}")
    else:
      print(f"Sorry, you will have to wash the dishes. Missing {money - self.money_payed} for completing the payment .")
