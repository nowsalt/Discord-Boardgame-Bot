# coding: utf-8

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import re


class BoardGame:

	def getIdFromText(text):
		url = "https://www.gamers-jp.com/playgame/db_searchlist.php?mode=1&order=1&search_flag=0&search_str=" + text + "&designer=0&maker=0&relyear=0&relyearb=0&player=%E6%9C%AA%E9%81%B8%E6%8A%9E&playerb=0&Submit=+++%E9%80%81%E4%BF%A1+++"
		response = requests.get(url)
		url = response.url
		id = "https://www.gamers-jp.com/playgame/db_gamea.php?game_id="
		if(id in url): return int(url.strip(id))
		response.encoding = response.apparent_encoding
		website = response.text
		try:
			df = pd.read_html(website, encoding="UTF-8")[9]
		except IndexError as ie:
			return None
		df.drop([0,1],axis=0,inplace=True)
		df.dropna(inplace=True)
		df.reset_index(drop=True,inplace=True)
		match = df[df[1]==text]
		if(len(match.index)):
			return match.values.tolist()[0][0]	
		else:
			return df.iat[1,0]


	def getNameFromText(text):
		url = "https://www.gamers-jp.com/playgame/db_searchlist.php?mode=1&order=1&search_flag=0&search_str=" + text + \
		"&designer=0&maker=0&relyear=0&relyearb=0&player=%E6%9C%AA%E9%81%B8%E6%8A%9E&playerb=0&Submit=+++%E9%80%81%E4%BF%A1+++"
		response = requests.get(url)
		response.encoding = response.apparent_encoding
		website = response.text
		try:
			df = pd.read_html(website, encoding="UTF-8")[9]
		except IndexError as ie:
			return None
		df.drop([0,1],axis=0,inplace=True)
		df.dropna(inplace=True)
		df.reset_index(drop=True,inplace=True)
		match = df[df[1]==text]
		if(len(match.index)):
			return match.values.tolist()[0][1]	
		else:
			return df.iat[1,1]


	def getGameList(page_num):
		url = "https://www.gamers-jp.com/playgame/db_lista.php?pageNum=" + str(page_num)
		df = pd.read_html(url)[11]
		bg_list = df[2:len(df)][0].to_list()
		return bg_list


	def getLastPage():
		url = "https://www.gamers-jp.com/playgame/db_newsa.php"
		df = pd.read_html(url)[5][2][0]
		last_page = int(re.sub(r"\D", "", df))
		return last_page


	def getGameTitle(id):
		url = "https://www.gamers-jp.com/playgame/db_gamec.php?game_id=" + str(id)
		df = pd.read_html(url)[2].iat[0,0]
		return df


	def getData1(id):
		url = "https://www.gamers-jp.com/playgame/db_gamea.php?game_id=" + str(id)
		df1 = pd.read_html(url)[11]
		df2 = pd.read_html(url)[17]
		df = pd.concat([df1, df2])
		return df


	def getData2(id):
		url = "https://www.gamers-jp.com/playgame/db_gameb.php?game_id=" + str(id)
		df = pd.read_html(url)[8]
		return df


	def getReview(id):
		url = "https://www.gamers-jp.com/playgame/db_gamec.php?game_id=" + str(id)
		df = pd.read_html(url)[9]
		return df
