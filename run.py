import sys
import os
from openai import OpenAI

client = OpenAI(api_key="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")
from urllib.parse import quote
from modules.Module_1.scraping import fetch_html
from modules.Module_2.processing import parse_article

# Initialize the OpenAI client with your API key

def save_summarized_data(article_info, summary, url):
    filename = quote(url, safe='')[7:200]  # Strip 'http://' and limit length
    filename += "_summarized.txt"
    processed_path = os.path.join('Data', 'processed', filename)

    os.makedirs(os.path.dirname(processed_path), exist_ok=True)

    # Format the article information for text output, including the summarized content
    article_str = f"Title: {article_info['title']}\nBy: {article_info['author']}\n\n{summary}"

    with open(processed_path, 'w', encoding='utf-8') as file:
        file.write(article_str)

    print(f"Saved summarized data to {processed_path}")

def main(url):
    html_content = fetch_html(url)
    if html_content:
        article_info = parse_article(html_content)
        
        # Adjust the prompt as necessary for your summarization task
        prompt = f"Summarize the following article in 50 words:\n\n{article_info['content']}"

        try:
            response = client.chat.completions.create(model="gpt-3.5-turbo",  # Use an appropriate model for your task
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ])
            summary = response.choices[0].message.content.strip()
            
            # Save the summarized content along with the article title and author
            save_summarized_data(article_info, summary, url)
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
    else:
        print("Failed to retrieve article.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run.py <URL>")
        sys.exit(1)
    
    article_url = sys.argv[1]
    main(article_url)
