# run.py

"""
This script serves as the entry point for the article scraping and processing application.
It integrates the scraping and processing modules to fetch, process, and save article information.

Functions:
    save_processed_data(article_info, url): Saves the processed article information in a structured format to a file.
    main(url): Orchestrates the fetching, processing, and saving of article data from a given URL.

The script exemplifies the use of modular design, separating concerns and making the system easier to understand and maintain.
"""

import sys
import json
import os
from urllib.parse import quote
from modules.Module_1.scraping import fetch_html
from modules.Module_2.processing import parse_article

def save_processed_data(article_info, url):
    # Generate a filesystem-safe filename based on the URL
    filename = quote(url, safe='')[7:200]  # Strip 'http://' and limit length
    filename += "_processed.txt"  # Ensure it ends with _processed.txt
    processed_path = os.path.join('Data', 'processed', filename)

    os.makedirs(os.path.dirname(processed_path), exist_ok=True)

    # Format the article information for text output
    article_str = f"Title: {article_info['title']}\nBy: {article_info['author']}\n\n{article_info['content']}"

    with open(processed_path, 'w', encoding='utf-8') as file:
        file.write(article_str)

    print(f"Saved processed data to {processed_path}")

# Ensure the main function and command line argument handling are as previously described


def main(url):
    html_content = fetch_html(url)
    if html_content:
        article_info = parse_article(html_content)
        save_processed_data(article_info, url)
    else:
        print("Failed to retrieve article.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run.py <URL>")
        sys.exit(1)
    
    article_url = sys.argv[1]
    main(article_url)
