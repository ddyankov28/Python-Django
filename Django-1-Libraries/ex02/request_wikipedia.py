import requests
import sys


def main():
    # English Wikipedia API
    url = "https://en.wikipedia.org/w/api.php"
    # define parameters for the search
    try:
        assert len(sys.argv) >= 2, "Parameter Absence"
        assert sys.argv[1].strip(), "Wrong/Empty Parameter"
        
        params = {
            # the action of the API (what to do)
            'action': 'opensearch',
            # what we search
            'search': sys.argv[1],
            'limit' : 1
        }
        response = requests.get(url, params=params)
        assert response, f"{response.raise_for_status()}"
        data = response.json()
        assert data[1], "Information not found"
        print(data)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    try:
        main()        
    except Exception as e:
        print("Error:", e)
