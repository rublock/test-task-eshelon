import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from select_dropdown import select_dropdown_func

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

# TODO тут надо сделать проверку, если тэг уже есть, то ничего не делать
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

dropdowns_dict = {
    "//input[@name='AddressType']/parent::div": "IPv4",
    "//input[@name='importanceType']/parent::div": "IMPORTANCE_TYPE_HIGH",
    "//input[@name='osType']/parent::div": "OPERATING_SYSTEM_TYPE_MACOS",
    "//input[@name='deviceType']/parent::div": "DEVICE_TYPE_TERMINAL",
}


def main():
    select_dropdown_func(driver, dropdowns_dict)


try:
    main()
except Exception as e:
    print(e)

driver.find_element(By.CLASS_NAME, "select-tag-input__icon").click()
driver.find_element(By.CLASS_NAME, "checkbox__icon").click()
driver.find_element(By.XPATH, "//button[text()='Создать']").click()

driver.find_element(By.XPATH, "//div[text()='Тестовый актив']").click()

time.sleep(20)
driver.quit()

if __name__ == "__main__":
    main()
