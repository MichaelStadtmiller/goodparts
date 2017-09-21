from bs4 import BeautifulSoup
import requests
from titlecase import titlecase
from .models import decades, alphabet
import os.path


def getURLS():
    posters = []
    for d in decades:
        for a in alphabet:
            # get posters for url
            posters.append(gethtml(d, a))
    return (posters)


def randomhtml():
    # get all urls from http://klipd.com/sitemap.php
    url = "http://klipd.com/random/"
    headers = {'Accept': 'text/css,*/*;q=0.1',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'gzip,deflate,sdch',
               'Accept-Language': 'en-US,en;q=0.8',
               'User-Agent': 'Mozilla/5 (Solaris 10) Gecko'}
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    # header
    head = soup.find('head')
    this_url = head.find('meta', attrs={'property': 'og:url'}).get('content').rsplit('/')

    m_name_path = this_url[len(this_url)-2].strip()
    s_name_path = this_url[len(this_url)-1].strip()
    m_name = titlecase(m_name_path.replace('-', ' ')).strip()
    s_name = titlecase(s_name_path.replace('-', ' ')).strip()

    # sidebar
    data = soup.find('div', attrs={'class': 'col-sm-4'})
    #a = data.find('div', attrs={'id': 'poster'})
    m_poster = data.find('img').get('src').strip()
    m_date_released = data.find('div', attrs={'class': 'movieReleaseTag'}).string[-10:].strip()
    descriptions = data.find('div', attrs={'id': 'clip-description'})
    dls = descriptions.find_all('dl')
    for dl in dls:
        if dl.find('dt').string == "Movie Description":
            m_description = dl.find('dd').string.strip()
            print('Movie - Description')
            print(m_description)
        elif dl.find('dt').string == "Clip Description":
            s_description = dl.find('dd').string.strip()
            print('Scene - description')
            print(s_description)
        elif dl.find('dt').string == "Director":
            m_director = dl.find('dd').string.strip()
        elif dl.find('dt').string == "Studios":
            m_studio = dl.find('dd').string.strip()

    #get video file

    return 200


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
    #   print(url)
    #   print("total: %s current: %s", str(total_movies_count), str(current_movie_count))
    #   need to click javascript button to get more movies before continuing
    #   get movie tags
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
