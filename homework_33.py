import requests
from bs4 import BeautifulSoup

request = requests.get("http://yermilovcentre.org/medias/")
soup = BeautifulSoup(request.content, "html.parser")

media_name = []
media_link = []
media_start_address = "http://yermilovcentre.org/"
pages_url = "http://yermilovcentre.org/medias/?page="


pages_qty = input("Input number of pages you need to parse (from 1 to 21): ")

num_of_page = int(pages_qty)
for index, index_page in enumerate(range(num_of_page)):
    pages_url = "http://yermilovcentre.org/medias/?page=" + str(index + 1)
    print(f"...parsing page ==> {pages_url}")
    request = requests.get(pages_url)
    soup = BeautifulSoup(request.content, "html.parser")

    for text in soup.select("a.row.title-text.mx-0.pt-3.pb-2"):
        media_name.append(text.text.strip())

    for link in soup.select("a.row.title-text.mx-0.pt-3.pb-2"):
        media_link.append(link.get("href"))

for counter, m_name in enumerate(media_name):
    print(f"\n{counter + 1}. {m_name} ({media_start_address}{media_link[counter]})")
