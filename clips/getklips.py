from bs4 import BeautifulSoup
import requests
from .models import decades


def getURLS():
    for d in decades:
        a = gethtml(d)
    return (a)


def gethtml(d):
    baseURL = "http://klipd.com/decade/"
    url = baseURL+d
    print(url)
    headers = {'Accept': 'text/css,*/*;q=0.1',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'gzip,deflate,sdch',
               'Accept-Language': 'en-US,en;q=0.8',
               'User-Agent': 'Mozilla/5 (Solaris 10) Gecko'}
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")

    # get the total movies for the decade
    total_movies_count = soup.find('h1', attrs={'class': 'entry-title'}).string.split(' ', 1)[0]
    print(total_movies_count)

    # count all movies on the page
    current_movie_count = len(soup.find_all('div', attrs={'class': 'poster'}))

    while current_movie_count < total_movies_count:
        # click the link

        current_movie_count = len(soup.find_all('div', attrs={'class': 'poster'}))

    posters = soup.find_all('div', attrs={'class': 'poster'})

    return posters
