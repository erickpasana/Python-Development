from bs4 import BeautifulSoup
import requests
# import lxml

comb_response = requests.get('https://news.ycombinator.com/')
yc_webpage = comb_response.text
comb_soup = BeautifulSoup(yc_webpage, 'html.parser')
# print(comb_soup)

# x--------------------------- Highest Title/Link -------------------------x
title_list = []
link_list = []
point_list = []
tag_list = comb_soup.find_all(name='td', attrs={'class': 'subtext'})
# print(tag_list)
for tag in tag_list:
    score = tag.find(name='span', attrs={'class': 'score'})
    if score == None:
        point_list.append(0)
    else:
        point_list.append(int(score.text.split()[0]))

for article in comb_soup.find_all(name='span', attrs={'class': 'titleline'}):
    title = article.a.text  #.find(name='span', attrs={'class': 'titleline'})
    title_list.append(title)
    link = article.a['href']
    link_list.append(link)

largest = max(point_list)
index = point_list.index(largest)
print(index)
print(title_list[index])
print(link_list[index])
print(point_list[index])



# td_class = comb_soup.find_all(name='td', class_='title')
# target_find_all = comb_soup.find(name='span', attrs={'class': 'titleline'})
# tr_id = comb_soup.find(name='tr', id='38789411')
# find_span = tr_id.find(name='span', attrs={'class': 'titleline'})
# print(find_span.a)
# print(find_span.a['href'])
# print(find_span.a.text)

# score = comb_soup.find(name='span', id='score_38789411')
# print(score.text)

# target_find_all = comb_soup.find(name='span', attrs={'class': 'titleline'})
# print(target_find_all)
# target_element = target_find_all.find('a')
# print(target_element)#.getText()
# print(target_find_all.a['href'])
# print(target_element.text)

# target_find_all = comb_soup.find_all(name='span', attrs={'class': 'titleline'})
# print(target_find_all[0])

# with open('website.html') as scrp_file:
#     web_contents = scrp_file.read()

# soup = BeautifulSoup(web_contents, 'html.parser')
# # com_url = soup.select_one("p a")
# com_url = soup.select("p a")
# print(com_url)
# print(com_url.get('href'))

# selector=



# class_heading = soup.find_all(name='h3', class_='heading')
# for tag in class_heading:
#     print(tag.getText())

# heading = soup.find(name='h1', id='name')
# print(heading.getText())

# all_tags = soup.find_all(name='a')
# for tag in all_tags:
#     print(tag.get('href'))

# all_tags = soup.find_all(name='a')
# for tag in all_tags:
#     print(tag.getText())

#, encoding="utf8"