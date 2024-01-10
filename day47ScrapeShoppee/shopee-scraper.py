from datetime import date
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#print date to help users to track down when the file was generated.
data = date.today()
data.strftime("%d/%m/%Y")
data1 = date.today()


# url = "https://shopee.ph/V380-Outdoor-CCTV-Dual-Camera-Wifi-Connect-To-Cellphone-With-Voice-Dual-Lens-Waterproof-Night-Visio-i.102443022.20790600795?xptdk=57d2ba34-1423-450b-a217-bfbd33d6798d"
url2 = "https://shopee.ph/V380-Outdoor-CCTV-Dual-Camera-Wifi-Connect-To-Cellphone-With-Voice-Dual-Lens-Waterproof-Night-Visio-i.102443022.20790600795?xptdk=57d2ba34-1423-450b-a217-bfbd33d6798d"
edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option('detach', True)
service = Service(executable_path=r"C:\Users\flpas\AppData\Local\Programs\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_option)
driver.get(url2)

# Find the button and click it
xpath = "//*[@id='main']/div/div[2]/div[1]/div[1]/div/div/section[1]/section[2]/div/div[4]/div/div[2]/div/section[1]/div/button[3]"
# button = driver.find_element(By.XPATH, xpath)  # replace 'button-id' with the actual id
button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))  # replace 'button-id' with the actual id
button.click()
# driver.execute_script("arguments[0].click();", button)
# Wait for the price to be updated
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pqTWkA'))) # replace 'price-class' with the actual class

# Now get the price
price = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div[1]/div/div/section[1]/section[2]/div/div[3]/div[2]/div/section/div/div[2]/div[1]").text
print(price)
driver.quit()
# sleep(3)
# driver.close()



# item_price = driver.find_element(By.CLASS_NAME, value="pqTWkA")
# item_price = driver.find_element(By.XPATH, value="//*[@id='main']/div/div[2]/div[1]/div[1]/div/div/section[1]/section[2]/div/div[3]/div[2]/div/section/div/div[2]/div[1]")
# item_price = driver.find_elements(By.CLASS_NAME, value="pqTWkA")
# print('x'*40)
# for i in item_price:
#     print(f"The price is; Php{i.text}")
#     print('x'*40)
