from elem import *
from elements import *


class Page():
    def __init__(self, element_class):
        assert isinstance(element_class, Elem)
        self.substr = element_class.__str__()
    
    def __str__(self):
        return self.substr
    
    
    def is_valid(self):
        return True


if __name__ == "__main__":
    try:
        page = Page(Html( [Head(), Body()] ))
        print(page)
    except Exception as e:
        print("Error: ", e)
