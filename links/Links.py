from urllib import parse
from bs4 import BeautifulSoup


def parse_link(response):
    soup = BeautifulSoup(response.content,"html.parser")
    anchor = soup.findAll(name="a")
    urls = set()
    for n in anchor:
        base_link = str(n.get("href"))
        if base_link.find("#") != 0:
            base_link = parse.urljoin(response.url, base_link, allow_fragments=True)
            urls.add(base_link)
    return urls
