from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://pythonscraping.com/pages/page3.html") # Pegando o html da pagina
bs = BeautifulSoup(html.read(), "html.parser") # Transformando o html em um objeto

for sibling in bs.find("table", {"id": "giftList"}).tr.next_siblings: # Pegando todos os filhos da tabela
    print(sibling)