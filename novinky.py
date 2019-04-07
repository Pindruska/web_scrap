"""
Program stahne ze serveru Novinky.cz poslednich sto clanku
z libovolne kategorie vcetne nazvu, autora, data vydani, obsahu a odkazu na clanek
"""
from bs4 import BeautifulSoup
import requests
from lxml import html
import re

page = requests.get('https://www.novinky.cz/archiv?id=7').text
soup = BeautifulSoup(page, 'lxml')

i = 0

for articles in soup.find_all('div', {'class' : ["item"]}): #najde vsechny clanky z archivu

	if i <100:
		print("Číslo článku: ", i + 1)

		headline = articles.h3.text #vypise z clanku nazev
		print("Název: ", headline)

		link = articles.find('a', attrs={'href' : re.compile("^https://")}) #vypise tu cast kodu s url adresou
		print("URL:", link.get('href')) #vytiskne cistou url adresu bez a a href apod.

		details = requests.get(link.get('href')).text
		more_soup = BeautifulSoup(details, 'lxml')

		release_time = more_soup.find('p', {'class' : ["publicDate"]}).text #vypise z clanku cas vydani
		print("Čas: ", release_time)

		author = more_soup.find('p', {'class' : ["articleAuthors"]}).text #vypise autora
		print("Autor: ", author)

		perex = more_soup.find('p', {'class' : ['perex']}).text #vypise to, co je pod nadpisem
		print("Text: ", perex)

		content = more_soup.find('div', {'class' : ["articleBody"]}).text #vypise text clanku
		print(content)
		print()
		print()

		i += 1
	
	else:
		break


