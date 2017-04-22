from bs4 import BeautifulSoup
import requests,urllib


url = 'https://downloads.skullsecurity.org/passwords/'
ext = 'txt.bz2'


def listFD(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

for file in listFD(url, ext):
    name =file.split("/")
    print(file)
    urllib.urlretrieve(file, "Files/"+name[len(name)-1])