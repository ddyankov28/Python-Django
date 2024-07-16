class HotBeverage:
    price = 0.3
    name = "hot beverage"

    def description(self):
        return "Just some hot water in a cup"
    
    def __str__(self):
        return (f"name : {self.name}\n"
                f"price : {self.price:.2f}\n"
                f"description : {self.description()}")


class Coffee(HotBeverage):
    price = 0.4
    name = "coffee"
    
    def description(self):
        return "A coffee, to stay awake"


class Tea(HotBeverage):
    name = "tea"
    

class Chocolate(HotBeverage):
    price = 0.5
    name = "chocolate"
    
    def description(self):
        return "Chocolate, sweet chocolate..."
    

class Cappuccino(HotBeverage):
    price = 0.45
    name = "cappuccino"
    
    def description(self):
        return "Un po' di Italia nella sua tazza!"

if __name__ == '__main__':
    try:
        hb = HotBeverage()
        print(hb)
        print("------------")
        coffee = Coffee()
        print(coffee)
        print("------------")
        tea = Tea()
        print(tea)
        print("------------")
        chocolate = Chocolate()
        print(chocolate)
        print("------------")
        cappuccino = Cappuccino()
        print(cappuccino)
        print("------------")
    except Exception as e:
        print("Error: ", e)
