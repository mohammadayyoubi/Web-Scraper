import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Set base URL
base_url = "http://quotes.toscrape.com/page/{}/"

# Step 2: Initialize variables
all_quotes = []  # list to collect all quotes
page = 1         # start from page 1

# Step 3: Loop until we collect at least 30 quotes (you can change the limit to 50 if needed)
while len(all_quotes) < 30:
    response = requests.get(base_url.format(page)) # y3ni http://quotes.toscrape.com/page/1/, /page/2/, etc.

    if response.status_code != 200:
        print(f"Page {page} not found. Stopping.")
        break

    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 4: Extract data -- 7a tjib kl quotes div
    quotes = soup.find_all('div', class_='quote')  # A list of BeautifulSoup objects, each representing a quote block on the page.

    if not quotes:  # ma la2a wala quote on this page
        print("No more quotes found.")
        break

    for quote in quotes:
        try:
            text = quote.find('span', class_='text').get_text(strip=True)  # 7a tfut 3la div qoute b3den el span yle 3ndo class text (howe el qoute text)
            author = quote.find('small', class_='author').get_text(strip=True) # same, enter small tag that have class author
            link = quote.find('a')['href'] # 7a tfut 3la a element w t7ot el href link
            full_link = "http://quotes.toscrape.com" + link #complete path of link of quote

            all_quotes.append([text, author, full_link])  # njma3 l quotes hon

            if len(all_quotes) >= 50:
                break  # basta 50 quotes

        except AttributeError as e:
            print(f"Skipping a quote due to missing element: {e}")

    page += 1  # move to next page

# Step 5: Write all quotes to CSV
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author', 'Link'])  # CSV header
    writer.writerows(all_quotes)  # write all rows at once

print(f"Scraping complete. {len(all_quotes)} quotes saved to output.csv.")
