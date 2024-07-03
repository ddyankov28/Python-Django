import sys


def find_capital():
    if len(sys.argv) != 2:
        return
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if sys.argv[1] not in states.keys():
        print("Unknown state")
        return
    print(capital_cities.get(states.get(sys.argv[1])))
    


if __name__ == '__main__':
    try:
        find_capital()
    except Exception as e:
        print("Error: ", e)
