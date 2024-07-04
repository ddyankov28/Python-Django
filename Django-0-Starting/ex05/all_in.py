import sys

def find_state(item, states, capital_cities):
    for abrreviation, capital in capital_cities.items():
        if item == capital:
            for state, abbr in states.items():
                if abbr == abrreviation:
                    return state



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
    list_args = sys.argv[1].split(",")
    for item in list_args:
        for state in states.keys():
            # print(f"This is the input {item.lower()}")
            # print(f"This is the state {state.lower()}")
            if item.lower() == state.lower():
                print(f"{capital_cities.get(states.get(state))} is the capital of {state}")
                continue
            for capital in capital_cities.values():
                if item.lower() == capital.lower():
                    state_var = find_state(item, states, capital_cities)
                    print(f"{capital} is the capital of {state_var}")
                    
                               
        

        



if __name__ == '__main__':
    try:
        all_in()
    except Exception as e:
        print("Error: ", e)