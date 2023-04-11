import requests
from bs4 import BeautifulSoup as BS

links = open("D:/IT/Orders/Parsing hudognik.net/links.txt",
             encoding="utf-8").read().split("\n")

s = requests.Session()
s.headers = {
    'cookie': 'PHPSESSID=08172f63270621d929dd3a2dc051e659; _ga=GA1.2.1333675620.1679226564; _gid=GA1.2.1878471261.1679226564; _ym_uid=167922656496407984; _ym_d=1679226564; _ym_isad=2; _ym_visorc=w; par1=vevefo3964@kaudat.com; par2=89fceeb8f8c39a4d10e4bfb3c3d253fa',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

name_selector = "body > div.container-fluid.mh500 > div > div.col-lg-9.col-md-9.col-xs-12 > div:nth-child(2) > h1"
city_selector = "body > div.container-fluid.mh500 > div > div.col-lg-9.col-md-9.col-xs-12 > div:nth-child(2) > div.mb_20 > div > div.col-sm-4.col-md-5.mb20 > ul:nth-child(1) > li:nth-child(2) > a"
country_selector = "body > div.container-fluid.mh500 > div > div.col-lg-9.col-md-9.col-xs-12 > div:nth-child(2) > div.mb_20 > div > div.col-sm-4.col-md-5.mb20 > ul:nth-child(1) > li:nth-child(1) > a"
phone_selector = "body > div.container-fluid.mh500 > div > div.col-lg-9.col-md-9.col-xs-12 > div:nth-child(2) > div.hudognik_menu > span"

for idx, link in enumerate(links[2757:]):
    r = s.get(f"https://hudognik.net{link}")
    html = BS(r.content, "html.parser")
    name = html.select_one(name_selector).text
    country = html.select_one(country_selector).text
    city = html.select_one(city_selector).text
    phone = html.select_one(phone_selector)

    print(idx, name)

    if phone is not None:
        with open("D:/IT/Orders/Parsing hudognik.net/data.txt", "a", encoding="utf-8") as f:
            f.write(f"{name}; {country}; {city}; {phone.text}\n")
