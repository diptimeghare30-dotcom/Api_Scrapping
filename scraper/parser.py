from bs4 import BeautifulSoup

def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    data = []

    for book in books:
        data.append({
            "title": book.h3.a["title"],
            "price": book.find("p", class_="price_color").text,
            "availability": book.find("p", class_="instock availability").text.strip(),
            "rating": book.find("p", class_="star-rating")["class"][1]
        })

    return data