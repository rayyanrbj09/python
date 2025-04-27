import threading
import requests
from bs4 import BeautifulSoup

# bs4 is usuallly used for web scraping

urls = [
    ' http://books.toscrape.com/',
    ' http://quotes.toscrape.com/',
    'https://fakestoreapi.com/products'
]

def fetch_content(urls):
    """Fetch content from a list of URLs and print the length of the content.
    Web scraping is the process of extracting data from websites.
    It involves sending a request to a web server, retrieving the HTML content of the page,
    and then parsing that content to extract the desired information.
    Multi-threading can be used to speed up the process of web scraping by allowing multiple requests to be sent simultaneously.
    """

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully fetched content from {url}")
            soup = BeautifulSoup(response.content, 'html.parser')
            print(f"Fetched content length: {len(soup.prettify())} characters")
            # You can add more processing of the soup object here
        else:
            print(f"Failed to fetch content from {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=([url],))
    threads.append(thread)
    thread.start()
    thread.join()  # Wait for the thread to finish before starting the next one