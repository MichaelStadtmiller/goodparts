from bs4 import BeautifulSoup
import requests
from .models import decades


def getURLS():
    baseURL = "http://klipd.com/decade/"
    for d in decades:
        myurl = baseURL+d
        a = gethtml(myurl)
    return (a)


def gethtml(url):
    print(url)
    headers = {'Accept': 'text/css,*/*;q=0.1',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'gzip,deflate,sdch',
               'Accept-Language': 'en-US,en;q=0.8',
               'User-Agent': 'Mozilla/5 (Solaris 10) Gecko'}
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    return soup
