import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://books.toscrape.com/"
response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
book_data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    book_data.append({
        "Title": title,
        "Price": price
    })
data = pd.DataFrame(book_data)
print("Extracted Book Details:")
print(data)
print("Total Books:",len(data))
data.to_csv("books_data.csv", index=False)
print("Book Data Saved Successfully!")
