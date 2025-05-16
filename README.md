# Web Scraper with BeautifulSoup

## Internship Task 2 - Scraping Static Data - BeautifulSoup

## 📌 Project Description
This Python script scrapes quotes, their authors, and detail page links from [quotes.toscrape.com](http://quotes.toscrape.com). The data is saved into a CSV file for easy access and analysis.

## 🌐 Website Chosen
**http://quotes.toscrape.com**  
This site was selected because it is:
- Static (no JavaScript rendering)
- Designed for scraping practice
- Clearly structured with predictable HTML tags

## ▶️ How to Run the Script

### Prerequisites:
- Python 3.x
- Libraries: `requests`, `beautifulsoup4`

### Setup Instructions:

```bash
pip install requests beautifulsoup4
python scraper.py
The results will be saved to output.csv.

🧩 Challenges or Observations
Understanding HTML tag structure was essential to select the correct tags for scraping.

Handling relative links required appending the base URL manually.

The website was well-suited and posed minimal issues.

📂 Output Sample (CSV)
Quote	Author	Link
“The world as we have created it...”	Albert Einstein	http://quotes.toscrape.com/author/Albert-Einstein

🔗 Submission
✅ Uploaded to GitHub: [Your GitHub Repo Link Here]

yaml
Copy
Edit

---

### 📤 **Publishing to GitHub**

1. Initialize Git:
```bash
git init
git add .
git commit -m "Initial commit for BeautifulSoup web scraping task"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/web-scraping-task
git push -u origin main
