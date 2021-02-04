import pytube
import os
import subprocess
import time
import urllib.request

from selenium import webdriver
from urllib import parse
from bs4 import BeautifulSoup

def get_url(input):
    url = 'https://www.youtube.com/results?search_query='
    url = url + parse.quote(input)

    driver = webdriver.Chrome('../lesson_han/chromedriver.exe')
    driver.get(url)

    bs = BeautifulSoup(driver.page_source, 'lxml')
    driver.close()

    return bs

def link_(bs):
    find_thumb = bs.select('a#video-title')

    link_list = []

    for data in find_thumb:
        link_list.append('{}{}'.format('https://www.youtube.com', data.get('href')))

    return link_list

def downloading(link_list):
    for data in link_list:
        tube = pytube.YouTube("{}".format(data))
        video = tube.streams.all()

        for i in range(len(video)):
            print(i,'번 :  ',video[i])

        img_qual = int(input("Choose the image quality number you want to download : "))

        DATA_DIR = './video'
        if not os.path.exists(DATA_DIR):
            os.mkdir(DATA_DIR)

        video[img_qual].download(DATA_DIR)

if __name__ == '__main__':
    try:
        input_ = input("Please enter a search : ")
        downloading(link_(get_url(input_)))
    except:
        print('error')