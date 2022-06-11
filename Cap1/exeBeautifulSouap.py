from urllib.request import urlopen 
from bs4 import BeautifulSoup

html = urlopen("https://www.aracagi.pb.gov.br/") # Pegando o html da pagina
bs = BeautifulSoup(html.read(), "html.parser") # Transformando o html em um objeto
print(bs.body.h1) # Pegando o h1 da pagina
print(bs.find_all("div")) # Pegando todos os divs da pagina