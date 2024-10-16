import sys
import requests
from bs4 import BeautifulSoup


def extract_next_link(url):
    print("---------------------")
    
    response = requests.get(url)
    assert response, f"{response.raise_for_status()}"
    soup = BeautifulSoup(response.text, 'html.parser')
    all_paragraphs = soup.find_all('p')
    #print(all_paragraphs)
    for paragraph in all_paragraphs:
        links = paragraph.find_all('a', href=True)
        new_link = print(links[0]['href'].split('/')[-1])
        break
    return new_link

def main():
    assert len(sys.argv) == 2, "Usage: python3 roads_to_philosophy.py <article>"
    start_article = sys.argv[1].replace(' ', '_').capitalize()
    current_article = start_article
    visited_articles = []
    while True:
        if current_article in visited_articles:
            raise Exception("It leads to an infinite loop !")
        visited_articles.append(current_article)
        if current_article == "Philosophy":
            raise Exception(f"{len(visited_articles)} roads from {start_article} to Philosophy")
        url = "https://en.wikipedia.org/wiki/" + current_article
        next_article = extract_next_link(url)
        print(f"Next Article : {next_article}\nCurrent Article : {current_article} ")
        current_article = next_article
        
    
    
    
    
    


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error: ", e)