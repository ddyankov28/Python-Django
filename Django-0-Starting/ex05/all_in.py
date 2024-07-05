import sys

def find_state(item, states, capital_cities):
    for abrreviation, capital in capital_cities.items():
        if item.lower() == capital.lower():
            for state, abbr in states.items():
                if abbr == abrreviation:
                    return state

def find_if_capital(states, capital_cities, item):
    for state in states.keys():
        if item.lower() == state.lower():
            print(f"{capital_cities.get(states.get(state))} is the capital of {state}")
            return True
    return False

def find_if_state(states, capital_cities, item):
    for capital in capital_cities.values():
        if item.lower() == capital.lower():
            state_var = find_state(item, states, capital_cities)
            print(f"{capital} is the capital of {state_var}")
            return True
    return False

def all_in():
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
    for item in sys.argv[1].split(","):
        item = item.strip()
        if not item:
            continue
        if find_if_capital(states, capital_cities, item):
            continue
        if find_if_state(states, capital_cities, item):
            continue
        print(f"{item} is neither a capital city nor a state")
                    
                               
if __name__ == '__main__':
    try:
        all_in()
    except Exception as e:
        print("Error: ", e)