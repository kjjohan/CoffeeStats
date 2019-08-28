from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#my_url ='https://en.wikipedia.org/wiki/Jacopo_Riccati'
my_url = 'https://kortladdning3.chalmerskonferens.se/CardLoad_Order.aspx'
# Creating a connection to the page
uClient = uReq(my_url)
# Reading the page
page_html = uClient.read()
uClient.close()
# Parse the html code
page_soup = soup(page_html, "html.parser")
print(page_soup.h1)