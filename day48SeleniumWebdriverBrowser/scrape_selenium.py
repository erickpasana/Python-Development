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
x_path = "//*[@id='content']/div/section/div[3]/div[2]/div/ul"
widget_ = driver.find_elements(By.XPATH, x_path)
print('x'*40)
data_dict = {}
# for i in widget_:
#     data_list.append(i.text.split('\n'))
for i in range(len(widget_)):
    pass

print(data_dict)
driver.quit()



# try:
#     # Wait for up to 10 seconds for the element to be present
#     widget_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2.icon-calendar")))
#     print(widget_.text)
# finally:
#     driver.quit()