import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Добавляем путь к директории drivers/chrome в переменную окружения PATH
os.environ["PATH"] += os.pathsep + "drivers/chrome"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://0.0.0.0/")
driver.implicitly_wait(10)

my_element = driver.find_element(By.CLASS_NAME, "license-expires-button-cancel")
my_element.click()

my_element = driver.find_element(By.CLASS_NAME, "header-menu__item")
my_element.click()

time.sleep(20)
driver.quit()
