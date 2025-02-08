from bs4 import BeautifulSoup
import requests as r

def save_html(html, path):                  # Saves html of webpage file locally
    with open(path, 'wb') as file:          # 'wb' is write bytes
        file.write(html)
    
save_html(r.content, 'google_com')

def open_html(path):                        # Open html file
    with open(path, 'rb') as file:          # 'rb' is read bytes
          return file.read()

html=open_html('google_com')


url = "https://tide.com/en-us/shop"

tide = r.get(url)

print(tide.content)                         # not working idk why gives me "AttributeError: module 'requests' has no attribute 'content'"