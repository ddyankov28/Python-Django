import requests
import sys
import dewiki


def main():
    # English Wikipedia API
    url = "https://en.wikipedia.org/w/api.php"
    assert len(sys.argv) == 2, "Usage: python3 request_wikipedia.py <search_term>"
    assert sys.argv[1].strip(), "Wrong/Empty Parameter"
    search_term = sys.argv[1]
    params = {
        'action'     : 'parse',
        'page'       : search_term,
        'format'     : 'json',
        'redirects'  : True,
    }
    response = requests.get(url, params=params)
    print(response.url)
    assert response, f"{response.raise_for_status()}"
    data = response.json()
    #print(data)
    page_text = data.get('parse').get('text').get('*')
    print(page_text
          )

if __name__ == "__main__":
    try:
        main()        
    except Exception as e:
        print("Error:", e)
