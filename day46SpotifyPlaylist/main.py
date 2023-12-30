import requests
from bs4 import BeautifulSoup

# time_factor = input("What time would you like to go to? YYYY-MM-DD")

url = 'https://www.billboard.com/charts/hot-100/2000-08-12'
response = requests.get(url)
billboard_wb = response.text
soup = BeautifulSoup(billboard_wb, 'html.parser')
titles = soup.select("div ul li ul h3")
titles_list = [item.text.strip() for item in titles]    #
print(type(titles))
print(titles_list)


# soup=BeautifulSoup(page.text,'html.parser')
# songs=soup.select("div ul li ul h3")
# song_list=[]
# for song in songs:
#     song_list.append(song.text.strip())
# print(song_list)