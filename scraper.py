import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send a GET request
url = "http://quotes.toscrape.com"
response = requests.get(url)

# Step 2: Parse HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract data
quotes = soup.find_all('div', class_='quote')

# Prepare CSV
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author', 'Link'])

    for quote in quotes:
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        link = quote.find('a')['href']
        full_link = url + link
        writer.writerow([text, author, full_link])

print("Scraping complete. Data saved to output.csv.")
