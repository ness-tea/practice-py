from bs4 import BeautifulSoup
import requests

def decodeWebPage():
    url = 'https://www.nytimes.com/'
    response = requests.get(url)
    html = BeautifulSoup(response.text, features="html.parser")

    print("The following are a list of articles shown on 'The New York Times' website:" + '\n')

    articles = ""
    for header in html.find_all('h2'):
        if (len(header.get('class')) >= 2):
            if (header.get('class')[0] == 'css-9ywo2s') or (header.get('class')[1] == 'esl82me2'):
                articles += (header.string + '\n')

    return articles

if __name__=="__main__":
    print(decodeWebPage())
    
    
