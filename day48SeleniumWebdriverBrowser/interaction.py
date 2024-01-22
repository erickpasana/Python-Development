from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from time import sleep

url = "https://en.wikipedia.org/wiki/Main_Page"
edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option('detach', True)
service = Service(executable_path=r"C:\Users\flpas\AppData\Local\Programs\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_option)
driver.get(url)
driver.implicitly_wait(10)
#----------------------------- Click Link ------------------------------x
# link_click = driver.find_element(By.LINK_TEXT, 'Mark Baldwin')
# link_click.click()

#----------------------------- Type Search ------------------------------x
# wait = WebDriverWait(driver, 10)
element = driver.find_element(By.CSS_SELECTOR, "a.cdx-button--fake-button--enabled span.vector-icon")
element.click()

sleep(1)
driver.implicitly_wait(10)
search_ = driver.find_element(By.NAME, value="search")
search_.send_keys("Python")#, Keys.ENTER
search_.submit()


# print(element.text)
# driver.quit()



# button_ = driver.find_element(By.CSS_SELECTOR, 'span vector-icon mw-ui-icon-search mw-ui-icon-wikimedia-search')
# button_.click()
# sleep(5)
# wait = WebDriverWait(driver, 10)
# print(widget_.text)
# widget_ = driver.find_element(By.CSS_SELECTOR, '#articlecount a')

# actions = ActionChains(driver)
# actions.move_to_element(element).perform()