import requests
from bs4 import BeautifulSoup as BS 

for i in range(1, 146):
    r = requests.get(f"https://hudognik.net/artists/page{i}/")
    html = BS(r.content, "html.parser")
    links = html.select(".pitem2 > div > div.col-sm-4.col-md-5.col-lg-4.col-xs-8.rcol > div:nth-child(1) > a")
    for link in links:
        with open("D:/IT/Orders/Parsing hudognik.net/links.txt", "a", encoding="utf-8") as f:
            print(i, link["href"])
            f.write(f'{link["href"]}\n')
