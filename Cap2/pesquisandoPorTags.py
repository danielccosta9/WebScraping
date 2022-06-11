from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://pythonscraping.com/pages/warandpeace.html") # Pegando o html da pagina
bs = BeautifulSoup(html.read(), "html.parser") # Transformando o html em um objeto

nomePersonagem = bs.find_all("span", {"class": "green"}) # Pegando todos os spans com a classe green
nome = bs.find_all("", {"class": "green"}) # Pegando todos com a classe green

falaPersonagem = bs.find_all("span", {"class": "red"}) # Pegando todos os spans com a classe red
fala = bs.find_all("", {"class": "red"}) # Pegando todos com a classe red

greenAndRed  = bs.find_all("span", {"class": ["green", "red"]}) # Pegando todos os spans com a classe green e red
pesquisando = bs.find_all("span", text="the prince") # Pegando todos os spans com o texto "the prince"
title = bs.find_all(id="title", class_="text") # Pegando o primeiro com o ID title e a classe text

for nome in nomePersonagem:
    print(f"Personagem: {nome.get_text()}") # Pegando o nome dos personagens dentra do span

for fala in falaPersonagem:
    print(f"Fala: {fala.get_text()}") # Pegando as falas dentro do span

print(len(pesquisando)) # Quantidade de elementos encontrados
print(title)

# Outra forma de fazer:
# for nome in bs.find_all("span", {"class": "green"}):
#     print(nome.get_text())
#
# for fala in bs.find_all("span", {"class": "red"}):
#     print(fala.get_text())