from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from pytz import NonExistentTimeError

try:
    html = urlopen("https://www.pythonscraping.com/pages/page1.html")  # Pegando o html da pagina
except HTTPError as e: # Tratando erros HTTP
    print(e) # Exibindo o erro
except URLError as e: # Tratando erros de URL
    print("The server could not be found!") # Se o servidor não for encontrado
else:
    print("It worked!") # Se tudo ocorrer bem
    bs = BeautifulSoup(html.read(), "html.parser") # Transformando o html em um objeto
    print(bs.find(NonExistentTimeError)) # Exibindo o erro