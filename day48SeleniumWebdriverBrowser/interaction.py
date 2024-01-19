from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

url = "https://en.wikipedia.org/wiki/Main_Page"
edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option('detach', True)
service = Service(executable_path=r"C:\Users\flpas\AppData\Local\Programs\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_option)
driver.get(url)
#----------------------------- Click Link ------------------------------x
# link_click = driver.find_element(By.LINK_TEXT, 'Mark Baldwin')
# link_click.click()

#----------------------------- Type Search ------------------------------x
wait = WebDriverWait(driver, 10)
# sleep(5)
# element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "vector-icon")))
element = driver.find_element(By.CSS_SELECTOR, "a.cdx-button--fake-button--enabled span.vector-icon")
element.click()
# actions = ActionChains(driver)
# actions.move_to_element(element).perform()
search_ = driver.find_element(By.NAME, value="search")
wait = WebDriverWait(driver, 10)
search_.send_keys("Python", Keys.ENTER)


# print(element.text)
# driver.quit()



# button_ = driver.find_element(By.CSS_SELECTOR, 'span vector-icon mw-ui-icon-search mw-ui-icon-wikimedia-search')
# button_.click()
# sleep(5)
# wait = WebDriverWait(driver, 10)
# print(widget_.text)
# widget_ = driver.find_element(By.CSS_SELECTOR, '#articlecount a')