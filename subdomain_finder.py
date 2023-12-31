import requests

domain = input("Enter Domain :")
file = open('word.txt','r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
    url1 = f"http://{subdomain}.{domain}"
    url2 = f"https://{subdomain}.{domain}"
    try:
        requests.get(url1)
        print(f"Discovered URL: {url1}")
        requests.get(url2)
        print(f"Discovered Url: {url2}")
    except requests.ConnectionError:
        pass