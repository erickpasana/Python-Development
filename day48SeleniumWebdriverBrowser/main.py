from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from time import sleep

url = "https://shopee.ph/V380-Outdoor-CCTV-Dual-Camera-Wifi-Connect-To-Cellphone-With-Voice-Dual-Lens-Waterproof-Night-Visio-i.102443022.20790600795?xptdk=57d2ba34-1423-450b-a217-bfbd33d6798d"
edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option('detach', True)
service = Service(executable_path=r"C:\Users\flpas\AppData\Local\Programs\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_option)
driver.get(url)

# button_ = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Dual Lens CCTV+64G']")
# button_.click()
# sleep(10)
# item_price = driver.find_element(By.XPATH, value="//*[@id='main']/div/div[2]/div[1]/div[1]/div/div/section[1]/section[2]/div/div[3]/div[2]/div/section/div/div[2]/div[1]")
item_price = driver.find_element(By.CSS_SELECTOR, "div.G27FPf")

print(item_price.text)
# driver.close()
# driver.quit()



# item_price = driver.find_element(By.CLASS_NAME, value="pqTWkA")
# item_price = driver.find_elements(By.CLASS_NAME, value="pqTWkA")
# print('x'*40)
# for i in item_price:
#     print(f"The price is; Php{i.text}")
#     print('x'*40)