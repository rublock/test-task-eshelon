import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

# Добавление тэга
driver.find_element(By.XPATH, "//div[text()='Инструменты']").click()
driver.find_element(By.XPATH, "//a[text()='Теги']").click()
driver.find_element(By.XPATH, "//span[text()='Добавить тег']").click()
driver.find_element(By.NAME, "Name").send_keys("Тестовый тэг")
driver.find_element(By.NAME, "Description").send_keys("Опистание тестового тэга")
driver.find_element(By.XPATH, "//button[text()='Создать']").click()

driver.find_element(By.XPATH, "//a[text()='Активы']").click()
driver.find_element(By.XPATH, "//button[text()='Добавить актив']").click()

driver.find_element(By.NAME, "name").send_keys("Тестовый актив")
driver.find_element(By.NAME, "Address").send_keys("147.45.235.190")

# TODO данный блок вывести в отдельный файл select_dropdown.py
try:
    dropdown_wrapper = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='AddressType']/parent::div"))
    )
    dropdown_wrapper.click()
except Exception as e:
    print(f"Ошибка при клике на обертку: {e}")

try:
    option_to_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "IPv4")))
    option_to_select.click()
except Exception as e:
    print(f"Ошибка: {e}")

importance_type_input = driver.find_element(By.NAME, "importanceType")
driver.execute_script("arguments[0].value = arguments[1];", importance_type_input, "Высокий")

os_type_input = driver.find_element(By.NAME, "osType")
driver.execute_script("arguments[0].value = arguments[1];", os_type_input, "MacOS")

device_type_input = driver.find_element(By.NAME, "deviceType")
driver.execute_script("arguments[0].value = arguments[1];", device_type_input, "терминал")

driver.find_element(By.CLASS_NAME, "select-tag-input__icon").click()
driver.find_element(By.CLASS_NAME, "checkbox__icon").click()
driver.find_element(By.XPATH, "//button[text()='Создать']").click()

driver.find_element(By.XPATH, "//div[text()='Тестовый актив']").click()

time.sleep(20)
driver.quit()
