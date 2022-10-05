import requests
from bs4 import BeautifulSoup

def main():
  standings_url = "https://fbref.com/es/comps/31/Estadisticas-de-Liga-MX"
  data = requests.get(standings_url)
  data.text
  print(data.text)


if __name__  == '__main__':
  main()
