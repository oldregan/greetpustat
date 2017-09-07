from bs4 import BeautifulSoup
import requests

def getlink(name):
    mainpath = "http://www.stat.purdue.edu/people/graduate_students/index.php"
    alt = "Picture of " + name
    r = requests.get(mainpath)
    soup = BeautifulSoup(r.text,"html.parser")
    for img  in soup.find_all('img'):
        if img.get('alt') == alt:
            fullurl = "www.stat.purdue.edu" + img.get('src')
            return fullurl
