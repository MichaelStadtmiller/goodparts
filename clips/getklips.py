from bs4 import BeautifulSoup
import requests
from titlecase import titlecase
from .models import *
import os.path


def getURLS():
    # next steps:
    # get all urls from http://klipd.com/sitemap.php
    # get actor profile, get all movies
    url = "http://klipd.com/random/"
    scrapeData(url)


def scrapeData(url):
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
    m_poster = data.find('img').get('src').strip()
    m_date_released = data.find('div', attrs={'class': 'movieReleaseTag'}).string[-10:].strip()
    descriptions = data.find('div', attrs={'id': 'clip-description'})
    dls = descriptions.find_all('dl')
    for dl in dls:
        if dl.find('dt').string == "Movie Description":
            m_description = dl.find('dd').string.strip()
        elif dl.find('dt').string == "Clip Description":
            s_description = dl.find('dd').string.strip()
        elif dl.find('dt').string == "Director":
            m_director = dl.find('dd').string.strip()
        elif dl.find('dt').string == "Studios":
            m_studio = dl.find('dd').string.strip()

    # get actors
    actor_list = data.find('div', attrs={'class': 'rowMM'})
    actors = actor_list.find_all('a')
    for a in actors:
        # actor names
        title_role = a.find('div', attrs={'class': 'castBlock'}).get('alt').split(' - ')
        a_name = title_role[0]
        r_role = title_role[1]

        a_headshot = a.get('href')

    # get video file
    ### I NEED SELENIUM.... :(
    return 200