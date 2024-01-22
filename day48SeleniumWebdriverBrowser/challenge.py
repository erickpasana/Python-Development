from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

#--------------------------------- Set-up ---------------------------------x
url = "https://secure-retreat-92358.herokuapp.com/"
edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option('detach', True)
service = Service(executable_path=r"C:\Users\flpas\AppData\Local\Programs\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_option)
driver.get(url)
driver.implicitly_wait(10)

f_name = driver.find_element(By.NAME, value='fName')
f_name.send_keys('Erick')
l_name = driver.find_element(By.NAME, value='lName')
l_name.send_keys('Pasana')
e_mail = driver.find_element(By.NAME, value='email')
e_mail.send_keys('flpasana@gmail.com')
button_ = driver.find_element(By.CSS_SELECTOR, 'form button')
button_.click()

