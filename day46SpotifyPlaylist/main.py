import requests
import csv
from bs4 import BeautifulSoup

# time_era = input("What time would you like to go to? YYYY-MM-DD\n")
time_era = '1983-03-29'

url = f"https://www.billboard.com/charts/hot-100/{time_era}"
response = requests.get(url)
billboard_wb = response.text
soup = BeautifulSoup(billboard_wb, 'html.parser')

#x--------------------------- tag-dot-class_label -----------------x
# title_soup = soup.select("div ul li ul h3")
# title_soup = soup.select("li.lrv-u-flex h3")
title_soup = soup.select("li h3.c-title")

titles_list = [item.text.strip() for item in title_soup]
# artist_soup = soup.select("div ul li ul p")
artist_soup = soup.select("span.a-no-trucate")  #c-label 
artist_list = [item.text.strip() for item in artist_soup]
# with open('to_college_era.csv', 'w', newline='') as songfile:
#     writer = csv.writer(songfile)
#     writer.writerow(["Rank", "Title", "Artist"])
#     for i in range(len(titles_list)):
#         writer.writerow([i+1, titles_list[i], artist_list[i]])

print(titles_list)
print(len(titles_list))
# print(artist_list)
# print(len(artist_list))


# soup=BeautifulSoup(page.text,'html.parser')
# songs=soup.select("div ul li ul h3")
# song_list=[]
# for song in songs:
#     song_list.append(song.text.strip())
# print(song_list)
# <span class="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet">
	
# 	Michael Jackson
# </span>