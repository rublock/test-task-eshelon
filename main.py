import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

os.environ["PATH"] += os.pathsep + "drivers/chrome"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://0.0.0.0/")
driver.implicitly_wait(10)

driver.find_element(By.NAME, "Login").send_keys("admin")
driver.find_element(By.NAME, "Password").send_keys("admin")
driver.find_element(By.CLASS_NAME, "button-submit").click()

driver.find_element(By.CLASS_NAME, "license-expires-button-cancel").click()
driver.find_element(By.CLASS_NAME, "header-menu__item").click()
driver.find_element(By.CLASS_NAME, "idbmXZ").click()

address_type_input = driver.find_element(By.NAME, "AddressType")
driver.execute_script("arguments[0].value = arguments[1];", address_type_input, "IPv4")

importance_type_input = driver.find_element(By.NAME, "importanceType")
driver.execute_script("arguments[0].value = arguments[1];", importance_type_input, "Высокий")

time.sleep(20)
driver.quit()
