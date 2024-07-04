import sys


def find_state():
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
    if sys.argv[1] not in capital_cities.values():
        print("Unknown capital city")
        return
    for abrreviation, capital in capital_cities.items():
        if sys.argv[1] == capital:
            for state, abbr in states.items():
                if abbr == abrreviation:
                    print(state)


if __name__ == '__main__':
    try:
        find_state()
    except Exception as e:
        print("Error: ", e)
