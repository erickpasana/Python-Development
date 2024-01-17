from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = "https://www.python.org/"
edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option('detach', True)
service = Service(executable_path=r"C:\Users\flpas\AppData\Local\Programs\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_option)
driver.get(url)

# x_path = "//*[@id='content']/div/section/div[3]/div[2]/div/h2"
# x_path = "//*[@id='content']/div/section/div[3]/div[2]/div/ul"
widget_time = driver.find_elements(By.CSS_SELECTOR, 'div.event-widget time')
widget_event = driver.find_elements(By.CSS_SELECTOR, 'div.event-widget li a')
print('x'*40)
event_dict = {}

for i in range(len(widget_time)):
    event_dict[i+1] = {
        'date': widget_time[i].text,
        'event': widget_event[i].text,
    }

print(event_dict)
driver.quit()
