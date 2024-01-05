import requests
import lxml
from bs4 import BeautifulSoup

# url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
url = "https://shopee.ph/V380-Outdoor-CCTV-Dual-Camera-Wifi-Connect-To-Cellphone-With-Voice-Dual-Lens-Waterproof-Night-Visio-i.102443022.20790600795?xptdk=bf906563-14d1-4089-af20-f7dc9c864f236"
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }

response = requests.get(url)    #, headers=header

# soup = BeautifulSoup(response.content, "lxml")
soup = BeautifulSoup(response.content, "html.parser")
product_name_soup = soup.select("div.c-_44qnta")
print(soup.prettify())

# price = soup.find(class_="a-offscreen").get_text()
# price_without_currency = price.split("$")[1]
# price_as_float = float(price_without_currency)
# print(price_as_float)