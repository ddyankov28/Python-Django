from elem import *
from elements import *


class Page():
    def __init__(self, element_class):
        assert isinstance(element_class, Elem)
        self.str = element_class.__str__()
    
    def __str__(self):
        return self.str
    
    
    def is_valid(self):
        return True


if __name__ == "__main__":
    try:
        page = Page(Html( [Head(), Body()] ))
        print(page)
        if page.is_valid():
            print("The Page is valid")
        else:
            print("The Page is not valid")
    except Exception as e:
        print("Error: ", e)
