import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.quotationspage.com/random.php")

soup = BeautifulSoup(response.content, "html.parser")
quotes = soup.find_all("dt", class_="quote")

print(quotes[0].getText())

