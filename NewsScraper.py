import requests
from bs4 import BeautifulSoup

# Function to scrape content, title, and author from a URL
def scrape_article_info(url, filename):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the article title
        article_title_elem = soup.find('h1', class_='headline__text inline-placeholder')
        article_title = article_title_elem.get_text().strip() if article_title_elem else "Title not found"
        # Find the author
        author_elem = soup.find('div', class_='headline__sub-text').find('span')
        author = author_elem.get_text().strip() if author_elem else "Author not found"
        # Find the article content
        article_content = soup.find('div', class_='article__content')
        # Extract text from the article content
        article_text = ''
        if article_content:
            article_text = '\n'.join([p.get_text() for p in article_content.find_all('p')])
        # Write the title, author, and content to a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"Title: {article_title}\n")
            file.write(f"By: {author}\n\n")
            file.write(article_text)
        print(f"Information scraped from {url} and saved to {filename}")
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Read URLs from the file
with open('article_urls.txt', 'r') as file:
    urls = file.readlines()

# Iterate through each URL and scrape information
for i, url in enumerate(urls, start=1):
    url = url.strip()  # Remove leading/trailing whitespaces
    filename = f'article_{i}.txt'
    scrape_article_info(url, filename)
