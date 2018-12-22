from bs4 import BeautifulSoup
import requests 

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
html = BeautifulSoup(requests.get(url).text, features='html.parser')

content_section = html.find_all(class_='content-section')

for section in content_section:
    if section.find_all('p') != []:
        for part in section.find_all('p'):
            print(part.text)
