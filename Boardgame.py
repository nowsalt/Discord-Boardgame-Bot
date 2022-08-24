# coding: utf-8

from importlib.abc import PathEntryFinder
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import re

def getGameList(page_num):
    url = "https://www.gamers-jp.com/playgame/db_lista.php?pageNum=" + page
    df = pd.read_html(url)[11]
    bg_list = df[2:len(df)][0].to_list()
    return bg_list

def getGameTite(id):
    url = "https://www.gamers-jp.com/playgame/db_gamec.php?game_id=" + id
    df = pd.read_html(url)[2]
    return df


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

page = "0"
print(getGameList(page))

id = "9614"
print(getGameTite(id))
print(getData1(id))
print(getData2(id))
print(getReview(id))