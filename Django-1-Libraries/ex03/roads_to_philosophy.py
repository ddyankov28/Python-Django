import sys
import requests
from bs4 import BeautifulSoup


def main():
    assert len(sys.argv) == 2, "Usage: python3 roads_to_philosophy.py <article>"
    start_article = sys.argv[1].replace(' ', '_').capitalize()
    current_article = start_article
    visited_articles = []
    while True:
        if current_article in visited_articles:
            raise Exception("It leads to an infinite loop !")
        print(current_article.replace('_', ' '))
        visited_articles.append(current_article)
        if current_article == "Philosophy":
            return (print(f"{len(visited_articles)} roads from {start_article.replace('_', ' ')} to Philosophy"))
        url = "https://en.wikipedia.org/wiki/" + current_article
        response = requests.get(url)
        assert response, "It's a dead end !"
        soup = BeautifulSoup(response.text, 'html.parser')
        all_paragraphs = soup.find_all('p')
        new_article = ""
        for paragraph in all_paragraphs:
            for link in paragraph.find_all('a'):
                href = link.get('href')
                if href and href.startswith('/wiki/') and not ':' in href:
                    new_article = href
                    break
            if new_article:
                break
        
        current_article = new_article.split("/wiki/")[1]
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Errror: ", e)