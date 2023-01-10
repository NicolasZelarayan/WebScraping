from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://play.livetables.io/roulette/?game_id=7&table_id=5001&limit_id=764589&identifier=1010800145ae9c56da939ea17ad681d181ecb8a7'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

num = soup.find_all('')
print(num)
print (page.status_code)