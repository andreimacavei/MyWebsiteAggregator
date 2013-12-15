import re

from urllib2 import urlopen
from urlparse import urljoin, urlsplit
import json

from bs4 import BeautifulSoup, UnicodeDammit
from bs4.element import Tag

def download(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    channel = soup.find("channel")

    items = [item for item in channel.find_all("item")]

    results = []

    for item in items:
        # Check if we get empty items
        if item.find('\n') == 0:
            import pdb; pdb.set_trace()

        entry = {}
        entry['title'] = item.title.get_text()
        entry['description'] = item.description.get_text()
        entry['link'] = item.link.get_text()
        entry['pubdate'] = item.pubdate.get_text()

        results.append(entry)

    return results

def write_json(filename, results):
    f = open(filename, "w")
    # f.write(codecs.BOM_UTF8)
    json.dump(results, f, indent=4, encoding="utf8")
    f.close()

if __name__ == '__main__':

    url = "http://feeds.bbci.co.uk/news/rss.xml"
    records = download(url)
    filename = "file.json"
    write_json(filename, records)