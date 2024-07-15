class HotBeverage:
    def __init__(self, price=0.30, name="hot beverage"):
        self.price = price
        self.name = name

    
    def description(self):
        return "Just some hot water in a cup"
    
    def __str__(self):
        return (f"name : {self.name}\n"
                f"price : {self.price:.2f}\n"
                f"description : {self.description()}")


class Coffee(HotBeverage):
    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def description(self):
        return super().description()

hb = HotBeverage()
print(hb)
print("------------")
coffee = Coffee(0.4, "coffee")
print(coffee)
