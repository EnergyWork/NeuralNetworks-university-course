import requests
from bs4 import BeautifulSoup

url = 'https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html'
r = requests.get(url)
if r.status_code != 200:
    print('error: request to pymorphy2 docs')
    exit(1)
else:
    print('success: request to pymorphy2 docs')
soup = BeautifulSoup(r.text, "html.parser")

with open("grammemes.json", "w", encoding='utf-8') as f:
    f.write(str(soup))
    print(soup)