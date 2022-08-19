# coding: utf-8

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import re

def getIds(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    elems = soup.find_all(class_="jimgbold")
    elems = elems[3:len(elems)-1]
    ids = []
    for elem in elems:
        id = re.sub(r"\D", "",elem.find('a').get('href'))
        ids += [id]
    return ids

def getData1(id):
    url = "https://www.gamers-jp.com/playgame/db_gamea.php?game_id=" + id
    df1 = pd.read_html(url)[11]
    df2 = pd.read_html(url)[17]
    df = pd.concat([df1,df2])
    return df

def getData2(id):
    url = "https://www.gamers-jp.com/playgame/db_gameb.php?game_id=" + id
    df = pd.read_html(url)[8]
    return df

def getReview(id):
    url = "https://www.gamers-jp.com/playgame/db_gamec.php?game_id=" + id
    df = pd.read_html(url)[9]
    return df

url = "https://www.gamers-jp.com/playgame/db_newsa.php?pageNum=0"
print(getIds(url))

id = "9614"
print(getData1(id))
print(getData2(id))
print(getReview(id))