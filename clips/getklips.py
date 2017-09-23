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
    url = 'http://klipd.com/watch/good-morning-vietnam/i-wont-forget-you-scene'
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

    # initialize
    m_description = ''
    s_description = ''
    m_director = ''
    m_studio = ''
    m_genres = ''

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

    # get video file
    flex_video = soup.find('div', attrs={'class': 'flex-video'})
    v = flex_video.find('script').get('data-config').split('/')
    s_video_path = 'https://cdn.video.playwire.com/' + v[3] + '/videos/' + v[6] + '/video-sd.mp4'

    # MOVIE TO DATABASE
    ## Check if exists
    m = Movie.objects.filter(name_path=m_name_path)
    if m:
        print('move ' + m_name + ' already exists in the database.')
    else:
        # Insert if DNE
        new_movie = Movie(name=m_name,
                          name_path=m_name_path,
                          description=m_description,
                          poster=m_poster,
                          studio=m_studio,
                          genres=m_genres,
                          date_released=m_date_released,
                          director=m_director)
        new_movie.save()
        m = new_movie

    # get actors
    actor_list = data.find('div', attrs={'class': 'rowMM'})
    actors = actor_list.find_all('a')
    for a in actors:
        # actor names
        title_role = a.find('div', attrs={'class': 'castBlock'}).get('alt').split(' - ')
        a_name = title_role[0]
        r_role = title_role[1]
        a_headshot = a.get('href')

        # ACTORS TO DATABASE
        ## Check if exists
        a = Actor.objects.filter(name=a_name)
        if a:
            print('actor ' + a_name + ' already exists in the database.')
        else:
            # Insert actor if DNE
            new_actor = Actor(name=a_name,
                              headshot=a_headshot)
            new_actor.save()
            a = new_actor

        r = Role.objects.filter(actor=a.objects, movie=m)
        if r:
            print('role ' + a_name + ' in ' + m_name + ' already exists in the database.')
        else:
            # Insert if DNE
            new_role = Role(movie=m,
                            actor=a,
                            role=r_role)
            new_role.save()




