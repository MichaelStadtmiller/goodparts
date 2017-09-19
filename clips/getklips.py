from bs4 import BeautifulSoup
import requests
from .models import decades, alphabet
import os.path

def getURLS():
    posters = []
    for d in decades:
        for a in alphabet:
            # get posters for url
            posters.append(gethtml(d, a))
    return (posters)


def gethtml(d, a):
    base_url = "http://klipd.com/decade"
    url = base_url + "/" + d + "/" + a
    headers = {'Accept': 'text/css,*/*;q=0.1',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'gzip,deflate,sdch',
               'Accept-Language': 'en-US,en;q=0.8',
               'User-Agent': 'Mozilla/5 (Solaris 10) Gecko'}
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")

    # get the total movies per decade per starting letter
    try:
        total_movies_count = soup.find('h1', attrs={'class': 'entry-title'}).string.split(' ', 1)[0]
    except:
        # debug if can't split
        print("nope")

    # if no movies, the first word is "Movies" not a number.
    if total_movies_count == "Movies":
        total_movies_count = 0
    else:
        total_movies_count = int(total_movies_count)

    ## MLS: NEED TO GET ALL MOVIES ##
    # count all movies on the page
    # current_movie_count = len(soup.find_all('div', attrs={'class': 'poster'}))
    # print if more movies behind a javascript button
    #if current_movie_count < total_movies_count:
    #    print(url)
    #    print("total: %s current: %s", str(total_movies_count), str(current_movie_count))
        # need to click javascript button to get more movies before continuing

    # get movie tags
    print(url)
    posters = soup.find_all('div', attrs={'class': 'poster'})
    movies = []
    for p in posters:
        # get initial movie data
        movie_name_path = p.find('a').get('href').rsplit('/')
        print(movie_name_path)
        movies.append(movie_name_path[len(movie_name_path)-2])
    print(movies)
    # loop through posters
    #   Get poster data: poster img, title, release date

    return soup
