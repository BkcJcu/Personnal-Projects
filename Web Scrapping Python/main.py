from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup as bs

url = "https://fr.wikipedia.org/wiki/Captain_Nazi"


options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get(url)

content = driver.page_source
soup = bs(content, 'html.parser')

prix = soup.find_all('p')
for i in prix:
    print(i.text)

driver.quit()
