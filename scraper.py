from bs4 import BeautifulSoup
import requests as r

url = "https://tide.com/en-us/shop"

def main():
    tide = r.get(url)

    soup = BeautifulSoup(tide.content, "html.parser")
    products = soup.find_all(class_="product-preview-title")
    descriptions = soup.find_all(class_="product-preview-description")
    price = soup.find_all(class_="ps-price")
    img = soup.find_all(class_="ps-product-image inline")

    print(products)      

if __name__ == "__main__":
    main()