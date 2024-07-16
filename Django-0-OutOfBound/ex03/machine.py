import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self):
        self.is_broken = False
        self.counter = 0

    class EmptyCup(HotBeverage):
        price = 0.9
        name = "empty cup"
        
        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self, message="This machine has to be repaired"):
            super().__init__(message)
    
    def repair(self):
        if self.is_broken == True:
            self.is_broken = False
            print("The coffee machine is now repaired")
            self.counter = 0
        else:
            print("No need to repair. Coffee machine still working")
    
    def serve(self, drink_class):
        try:
            if self.counter == 10:
                self.is_broken = True
                raise self.BrokenMachineException
            assert issubclass(drink_class, HotBeverage), "The class should derive from HotBeverage"
            ret = random.choice([drink_class, self.EmptyCup])()
            print(f"The Coffee machine served {ret.name}")
            self.counter += 1
            return ret
        except self.BrokenMachineException as e:
            print("Machine Error: ", e)
        
# class Vodka:
#     pass

if __name__ == '__main__':
    try:
        machine = CoffeeMachine()
        
        machine.serve(Coffee)
        machine.serve(Tea)
        machine.serve(Cappuccino)
        machine.serve(Chocolate)
        machine.serve(Tea)
        machine.serve(Tea)
        machine.serve(Cappuccino)
        machine.serve(Chocolate)
        machine.serve(Coffee)
        machine.serve(Cappuccino)
        print("---------------")
        machine.serve(Coffee)
        #machine.serve(Vodka)
        machine.serve(Coffee)
        print("---------------")
        machine.repair()
        machine.serve(Coffee)
        machine.repair()
        #machine.serve(Vodka)
        machine.serve(Cappuccino)
        for i in range(10):
            machine.serve(random.choice([Coffee, Tea, Chocolate, Cappuccino]))
        machine.repair()
        machine.serve(Coffee)
    except Exception as e:
        print("Error: ", e)

