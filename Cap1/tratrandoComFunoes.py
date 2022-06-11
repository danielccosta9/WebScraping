from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def getTitle(url): # Função que pega o titulo da pagina
    try:
        html = urlopen(url) # Pegando o html da pagina
    except HTTPError as e:  # Tratando erros HTTP
        return None
    try:
        bs = BeautifulSoup(html.read(), "html.parser") # Transformando o html em um objeto
        title = bs.body.h1 # Pegando o h1 da pagina
    except AttributeError as e: # Tratando erros de atributo
        return None
    return title # Retornando o titulo

title = getTitle("https://www.pythonscraping.com/pages/page1.html") # Definindo a url da pagina

if title == None: # Se o titulo for None
    print("Title could not be found")
else: # Se o titulo não for None
    print(title) # Exibindo o titulo
    print(title.get_text()) # Pegando o texto do h1