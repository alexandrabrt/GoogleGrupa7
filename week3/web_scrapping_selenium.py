from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get('https://www.bnr.ro/files/xml/nbrfxrates2022.htm')
# //*[@id="Data_table"]
table = browser.find_element(by=By.XPATH, value='//*[@id="Data_table"]')
table_text = table.text
lista = table_text.split('\n')
print(lista)
# //*[@id="Data_table"]/table/thead/tr
header_len = browser.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead/tr')
print(header_len.text)
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        if '-' in lista[i]:
            dictionar[header[int(j)]].append(lista[i])
        else:
            dictionar[header[int(j)]].append(float(lista[i]))
print(dictionar)
df = pd.DataFrame(dictionar)
df.to_excel('BNR_ALL_DATA.xlsx')

