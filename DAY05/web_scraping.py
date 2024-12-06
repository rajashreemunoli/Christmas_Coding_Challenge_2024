import requests
from bs4 import BeautifulSoup

def scrape_quotes():
     # URL of the site designed for scraping
    url = "http://quotes.toscrape.com/"

    # Send a GET request to fetch the webpage content
    response=requests.get(url)
    if response.status_code!=200:
        print(f'Failed to fetch page: {response.status_code}')
        return
    # Parse the HTML content
    soup=BeautifulSoup(response.text,"html.parser")

    # Find all quotes on the page
    quotes=soup.find_all("div",class_="quote")

    print("\nQuotes from the Page:")
    print("-" * 50)

    # Extract quotes and their authors
    for quote in quotes:
        text=quote.find("span",class_="text").text
        author=quote.find("small",class_="author").text
        print(f"Quote: {text}")
        print(f"Author: {author}")
        print("-" * 50)

if __name__ == "__main__":
    scrape_quotes()