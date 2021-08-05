import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = input("Enter site for crawling (e.g. google.com): ")
subdomains = []

with open("subdomains.txt", 'r') as file:
    for line in file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        subdomains.append("https://" + test_url)

        if response:
            print("Subdomain {} exists!!".format("https://" + test_url))

with open("subdomain.csv", "r+") as f:
    f.writelines(f'\n{target_url}, {subdomains}')
