# === Imports / Libraries ===
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine

# === Configurations  ===

# === def functions ===
def scrape_books(url='http://books.toscrape.com/'):
    books = []
    while url:
        res = requests.get(url)
        res.encoding = 'utf-8'  # ✅ fix encoding issue
        soup = BeautifulSoup(res.text, 'html.parser')
        articles = soup.select('article.product_pod')

        for book in articles:
            title = book.h3.a['title']
            price_str = book.select_one('.price_color').text.strip().replace('£', '')  # ✅ clean price
            price = float(price_str)
            rating = book.p['class'][1]
            books.append({'title': title, 'price': price, 'rating': rating})

        next_btn = soup.select_one('li.next a')
        url = 'http://books.toscrape.com/' + next_btn['href'] if next_btn else None

    return pd.DataFrame(books)

df_books = scrape_books()
df_books.to_csv("books_raw.csv", index=False)

# === Load raw Data into PostgreSQL Database ===
# engine = create_engine('')
# df_books.to_sql('books_raw', engine, if_exists='replace', index=False)
