import requests
import re
from urllib.parse import urljoin


target_url = "http://" + input("Enter a website crawling: ")


def extract_links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode('utf8'))


href_link = extract_links(target_url)

for link in href_link:
    link = urljoin(target_url, link)
    print(link)
