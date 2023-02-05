import requests
from bs4 import BeautifulSoup as bs

def parser():
    r = requests.get("https://www.anekdot.ru/random/anekdot/")
    soup = bs(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    text_anekdots = [c.text for c in anekdots]
    return text_anekdots
anekdot = parser()[0]