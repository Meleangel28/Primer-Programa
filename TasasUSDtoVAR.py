import requests
from bs4 import BeautifulSoup

URL = "https://www.google.com/search?q=usd+to+clp&rlz=1C1CHBD_esVE816VE816&oq=usd+to+clp&aqs=chrome..69i57j0l7.3623j0j4&sourceid=chrome&ie=UTF-8"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
#HAY QUE EDITAR LA RUTA.
results = soup.find(id="DFlfde SwHCTb")
print(results)