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
        'action'     : 'query',
        'titles'     : search_term,
        'prop'     : 'revisions',
        'rvprop'  : 'content',
        'format'  : 'json',
        'redirects' : True
    }
    response = requests.get(url, params=params)
    print("Response URL: ", response.url)
    assert response, f"{response.raise_for_status()}"
    data = response.json()
    page = next(iter(data['query']['pages'].values()))
    assert 'revisions' in page, "No info for this search term"
    page_text = page['revisions'][0]['*']
    plain_text = dewiki.from_string(page_text).strip()
    file = open(f"{search_term}.wiki", "w")
    file.write(plain_text)
    file.close()

    # plain_text = dewiki.from_string(page_text)
    # print(plain_text)
if __name__ == "__main__":
    try:
        main()        
    except Exception as e:
        print("Error:", e)
