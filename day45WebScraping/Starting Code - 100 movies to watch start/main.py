import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movies_webpage = response.text
soup = BeautifulSoup(movies_webpage, 'html.parser')
titles = soup.find_all(name='h3', attrs={'class': 'title'})
titles_only = []

for title in titles:
    titles_only.append(title.text)
# titles_only_sorted = list(reversed(titles_only))
titles_only_sorted = titles_only[::-1]

with open('movie_list.txt', 'w', encoding='utf-8') as file:
    # Loop through the list and write each element to the file, followed by a newline
    for movie in titles_only_sorted:
        file.write(f"{movie}\n")

print(titles_only_sorted)

