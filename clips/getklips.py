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

    #error catch
    try:
        if soup.find('div', attrs={'class': 'alert'}).string == "Sorry, clip not found.":
            return 500
    except:
        pass

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
    if m_date_released == '0000-00-00':
        m_date_released = None

    # initialize
    m_description = ''
    s_description = ''
    m_director = ''
    m_studio = ''
    m_genres = ''

    descriptions = data.find('div', attrs={'id': 'clip-description'})
    dls = descriptions.find_all('dl')
    for dl in dls:
        if dl.find('dt').string == 'Movie Description':
            try:
                m_description = dl.find('dd').string.strip()
            except AttributeError:
                m_description = ''
        elif dl.find('dt').string == 'Clip Description':
            try:
                s_description = dl.find('dd').string.strip()
            except AttributeError:
                s_description = ''
        elif dl.find('dt').string == 'Director':
            try:
                m_director = dl.find('dd').string.strip()
            except AttributeError:
                m_director = ''
        elif dl.find('dt').string == 'Studios':
            try:
                m_studio = dl.find('dd').string.strip()
            except AttributeError:
                m_studio = ''

    try:
        # get video file
        flex_video = soup.find('div', attrs={'class': 'flex-video'})
        v = flex_video.find('script').get('data-config').split('/')
        s_video_path = 'https://cdn.video.playwire.com/' + v[3] + '/videos/' + v[6] + '/video-sd.mp4'
    except AttributeError:
        s_video_path = ''


    # MOVIE TO DATABASE
    ## Check if exists
    if Movie.objects.filter(name_path=m_name_path):
        pass
        #print('movie ' + m_name + ' already exists in the database.')
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
        print('movie ' + m_name + ' Added!')

    if Scene.objects.filter(name_path=s_name_path):
        pass
        #print('scene ' + s_name + ' already exists in the database.')
    else:
        # Insert if DNE
        new_scene = Scene(movie=Movie.objects.get(name=m_name),
                          name=s_name,
                          name_path=s_name_path,
                          description=s_description,
                          video_path=s_video_path)
        new_scene.save()
        print('scene ' + s_name + ' Added!')


    # get actors
    actor_list = data.find('div', attrs={'class': 'rowMM'})
    actors = actor_list.find_all('a')
    for a in actors:
        # actor names
        try:
            actor_data = a.find('div', attrs={'class': 'castBlock'})
            title_role = actor_data.get('alt').split(' - ')
            a_name = title_role[0]
            r_role = title_role[1]
        except AttributeError:
            a_name = ''
            r_role = ''

        try:
            a_headshot = actor_data.get('style').split('(''')[1][:-3][1:]
        except AttributeError:
            a_headshot = ''

        try:
            a_url = a.get('href')
        except AttributeError:
            a_url = ''

        # ACTORS TO DATABASE
        ## Check if exists
        if Actor.objects.filter(name=a_name):
            pass
            # print('actor ' + a_name + ' already exists in the database.')
        else:
            # Insert actor if DNE
            new_actor = Actor(name=a_name,
                              url=a_url,
                              headshot=a_headshot)
            new_actor.save()
            print('actor ' + a_name + ' Added!')

        if Role.objects.filter(actor__name=a_name).filter(movie__name=m_name):
            pass
            # print('role ' + a_name + ' in ' + m_name + ' already exists in the database.')
        else:
            # Insert if DNE
            # error catch in case movie or actor is not added
            thismovie = Movie.objects.get(name=m_name)
            thisactor = Actor.objects.get(name=a_name)
            new_role = Role(movie=thismovie,
                            actor=thisactor,
                            role=r_role)
            new_role.save()
            print('role ' + a_name + ' in ' + m_name + ' Added!')




