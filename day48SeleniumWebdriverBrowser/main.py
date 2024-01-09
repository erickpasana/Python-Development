from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep

edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option('detach', True)
service = Service(executable_path=r"C:\Users\flpas\AppData\Local\Programs\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_option)
driver.get('https://www.amazon.com')

sleep(3)
# driver.close()
driver.quit()