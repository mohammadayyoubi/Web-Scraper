import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send a GET request
url = "http://quotes.toscrape.com"
response = requests.get(url)

# Step 2: Parse HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract data -- 7a tjib kl quotes div
quotes = soup.find_all('div', class_='quote')

# Prepare CSV
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author', 'Link'])

    #loop to path 3la each quote extacted
    for quote in quotes:
        text = quote.find('span', class_='text').get_text(strip=True)  # 7a tfut 3la div qoute b3den el span yle 3ndo class text (howe el qoute text)
        author = quote.find('small', class_='author').get_text(strip=True) # same, enter small element that have class author
        link = quote.find('a')['href'] # 7a tfut 3la a element w t7ot el href link
        full_link = url + link #complete path of link of quote
        # Step 4: Write to CSV
        writer.writerow([text, author, full_link])

print("Scraping complete. Data saved to output.csv.")
