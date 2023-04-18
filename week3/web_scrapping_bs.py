from bs4 import BeautifulSoup
import requests

# request_page = requests.get('https://www.bnr.ro/files/xml/nbrfxrates2021.htm')
request_page = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
print(request_page)
link = BeautifulSoup(request_page.text, 'html.parser')
print(link)
