from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://pythonscraping.com/pages/page3.html") # Pegando o html da pagina
bs = BeautifulSoup(html.read(), "html.parser") # Transformando o html em um objeto

print(bs.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()) # Pegando o texto anterior ao img1