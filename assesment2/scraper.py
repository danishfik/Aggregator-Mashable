import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin

def scrape_mashable():
    url = "https://sea.mashable.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        articles = []

        # Limit the loop to scrape a maximum of 100 articles
        index = 0
        for element in soup.find_all("a", class_="box_title"):
            if index >= 100:
                break

            title = element.get_text(strip=True)
            link = urljoin(url, element["href"])
            articles.append({"title": title, "link": link})

            index += 1

        return articles
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return []

if __name__ == "__main__":
    articles = scrape_mashable()
    for article in articles:
        print(f"{article['title']} - {article['link']}")
