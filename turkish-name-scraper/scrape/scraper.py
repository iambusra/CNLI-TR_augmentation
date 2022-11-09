import requests
from bs4 import BeautifulSoup as bs

def get_link_content(hyperlink):
	r = requests.get(hyperlink)
	soup = bs(r.content, features="html.parser")

	return soup.prettify()


def get_links(hyperlink):
	r = requests.get(hyperlink)
	soup = bs(r.content, features="html.parser")

	return [link.get('href') for link in soup.findAll('a') if link.get('href') is not None]
