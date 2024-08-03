import requests
import json
import sys
import dewiki


def main():
    # Wikipedia API
    url = "https://en.wikipedia.org/w/api.php"
    # define parameters for the search
    try:
        assert len(sys.argv) == 2, "Wrong number of args"
        assert sys.argv[1].strip(), "Wrong argument"
        
        params = {
            # the action of the API (what to do)
            'action': 'parse',
            # what we search
            'page': sys.argv[1],
            # request the wikitext of the page
            'prop': 'wikitext',
            # the response format (most cases json) 
            'format': 'json',
            # if no result gives suggestions and redirects to sth else
            'redirects': True
        }
        response = requests.get(url, params=params)
        #print(response.status_code)
        assert response.ok, f"{response.raise_for_status()}"
        data = response.json()
        #print(data['parse']['wikitext']['*'])
        res = dewiki.from_string(data['parse']['wikitext']['*'])
        file = open(sys.argv[1] + ".wiki", "w")
        file.write(res)
        response.close()
        file.close()
    except Exception as e:
        print(e)
if __name__ == "__main__":
    try:
        main()        
    except Exception as e:
        print("Error:", e)
