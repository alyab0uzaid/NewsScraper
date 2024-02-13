# News Scraper

News Scraper is a Python script that scrapes article content, titles, and authors from a list of URLs provided in a text file. It utilizes the BeautifulSoup library for web scraping and requires Python 3.x to run.

# Features
- Scrapes article content, titles, and authors from a list of URLs.
- Saves the scraped information to individual text files.
- Generates a Conda environment file (requirements.yml) for easy environment setup.

# Usage
Prerequisites
- Python 3.x installed on your system.
- Conda package manager installed (optional, but recommended for managing Python environments).

# Setup
1. Clone this repository to your local machine:

- git clone https://github.com/alyab0uzaid/NewsScraper/

2. Navigate to the project directory:

- cd NewsScraper

3. Create a Conda environment and install dependencies:

- conda env create -f requirements.yml
This will create a Conda environment named news-scraper with the required dependencies.

4. Activate the Conda environment:


- conda activate NewsScraper

# Running the Script
1. Prepare a text file (article_urls.txt) containing a list of URLs you want to scrape. Each URL should be on a separate line.

2. Run the Python script (NewsScraper.py) with the following command:
- python3 NewsScraper.py
This will scrape the articles from the URLs provided in article_urls.txt and save the information to individual text files.

# Output
The scraped information (title, author, and content) for each article will be saved to individual text files with filenames in the format article_<index>.txt.

