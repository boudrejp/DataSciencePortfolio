### web scraper to take in data from ESPN Rugby StatsGuru
### author: boudrejp
### url: http://stats.espnscrum.com/statsguru/rugby/stats/index.html?class=1;page=1;spanmax1=08+Nov+2017;spanmax2=08+Nov+2017;spanmin1=08+Nov+2007;spanmin2=08+Nov+2015;spanval1=span;spanval2=span;template=results;type=player;view=match
### can simply loop thru page numbers: this query gives 1061 pages of results


import time
from time import sleep
from datetime import datetime
from random import randint
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.request import Request, urlopen
from urllib.error import URLError

###all of the variables that we'll be importing
player_list = []
country_list = []
position_list = []
points_list = []
tries_list = []
conv_list = []
pens_list = []
drops_list = []
result_list = []
opp_list = []

###track the error iterateration -> we can go back and get these later

print('libraries successfully imported')

def table_url_page(page):
	return('http://stats.espnscrum.com/statsguru/rugby/stats/index.html?class=1;page=' + str(page) +
	';spanmax1=08+Nov+2017;spanmax2=08+Nov+2017;spanmin1=08+Nov+2007;spanmin2=08+Nov+2015;' + 
	'spanval1=span;spanval2=span;template=results;type=player;view=match')

##will need to loop for all pages
##use a time delay to not use up too many server resources
page_range = range(1,1601+1)

time_start = datetime.now()

for i in page_range:
	req = Request(table_url_page(i))
	try:
		response = urlopen(req)
	except URLError as e:
		if hasattr(e, 'reason'):
			print('We failed to reach a server.')
			print('Reason: ', e.reason)
		elif hasattr(e, 'code'):
			print('The server couldn\'t fulfill the request.')
			print('Error code: ', e.code)
	else:
		sleep(randint(5,30))
		
		with urlopen(table_url_page(i)) as url:
			s = url.read()
		
		soup = BeautifulSoup(s)
		#print(soup)
		table_entries = soup.find_all("tr", class_="data1")
		###returned is a list of all the HTML that is under this class...
		###each instance is saved as a separate entry
		#print(letters[1])
		entries_on_page = len(table_entries)
		#print(entries_on_page)
		
		###now, to trim the data into the categories that we want
		###for loop for each entry in the table on the given page. store all the values
		for j in range(len(range(1,entries_on_page + 1))):
			entry = table_entries[j]
			player = entry.find("a", class_="data-link").get_text()
			player = str(player)

			country = entry.find("i").get_text()
			country = str(country)
			##get rid of parentheses around country abbreviation
			country = country.replace("(", "")
			country = country.replace(")", "")

			position = entry.find_all("td", class_="left")[1].get_text()
			position = str(position)

			points_scored = entry.find("b").get_text()
			points_scored = str(points_scored)

			tries_scored = entry.find_all("td")[3].get_text()
			tries_scored = str(tries_scored)

			conversions_scored = entry.find_all("td")[4].get_text()
			conversions_scored = str(conversions_scored)

			penalties_scored = entry.find_all("td")[5].get_text()
			penalties_scored = str(penalties_scored)

			drops_scored = entry.find_all("td")[6].get_text()
			drops_scored = str(drops_scored)

			result = entry.find_all("td", class_="left")[2].get_text()
			result = str(result)

			opposition = entry.find_all("td", class_="left")[3].get_text()
			opposition = str(opposition)
			opposition = opposition.replace("v ", "")

			#print("Player is " + player)
			#print("Country is " + country)
			#print("Position is " + position)
			#print("Scored " + points_scored + " points")
			#print("Scored " + tries_scored + " tries")
			#print("Scored " + conversions_scored + " conversions")
			#print("Scored " + penalties_scored + " pens") 
			#print("Scored " + drops_scored + " drop goals")
			#print("Result of game was " + result)
			#print("The opposition was " + opposition)

			player_list.append(player)
			country_list.append(country)
			position_list.append(position)
			points_list.append(points_scored)
			tries_list.append(tries_scored)
			conv_list.append(conversions_scored)
			pens_list.append(penalties_scored)
			drops_list.append(drops_scored)
			result_list.append(result)
			opp_list.append(opposition)
			
		time_loop = datetime.now()
		print("Loop " + str(i) + " completed. Total runtime so far: " + str(time_loop - time_start))
		
		if i % 5 == 0:
			rugby_df_temp = pd.DataFrame(
				{"player": player_list,
				 "country": country_list,
				 "position": position_list,
				 "points": points_list,
				 "tries": tries_list,
				 "conv": conv_list,
				 "penalties": pens_list,
				 "drop_kicks": drops_list,
				 "result": result_list,
				 "opposition": opp_list
				})

			rugby_df_temp.to_csv('testpage.csv', index = False)
			print("CSV created with all data from " + str(i) + " iterations")

		
time_end = datetime.now()
time_taken = time_end - time_start

print("Time taken: " + str(time_taken))

rugby_df_final = pd.DataFrame(
    {"player": player_list,
     "country": country_list,
     "position": position_list,
     "points": points_list,
     "tries": tries_list,
     "conv": conv_list,
     "penalties": pens_list,
     "drop_kicks": drops_list,
     "result": result_list,
     "opposition": opp_list
    })

rugby_df_final.to_csv('rugby_stats_final.csv', index = False)

