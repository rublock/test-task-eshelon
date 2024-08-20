import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from delete_assets import delete_assets_func
from select_dropdown import select_dropdown_func


class WebDriver:
    def __init__(self):
        os.environ["PATH"] += os.pathsep + "drivers/chrome"
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--allow-insecure-localhost")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)

    def get(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def find_element(self, by, value):
        return self.driver.find_element(by, value)


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, username: str, password: str):
        self.driver.find_element(By.NAME, "Login").send_keys(username)
        self.driver.find_element(By.NAME, "Password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "button-submit").click()


class TagManager:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_tag(self, tag_name: str, description: str):
        self.driver.find_element(By.XPATH, "//div[text()='Инструменты']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Теги']").click()

        if not self.is_tag_present(tag_name):
            self.driver.find_element(By.XPATH, "//span[text()='Добавить тег']").click()
            self.driver.find_element(By.NAME, "Name").send_keys(tag_name)
            self.driver.find_element(By.NAME, "Description").send_keys(description)
            self.driver.find_element(By.XPATH, "//button[text()='Создать']").click()

    def is_tag_present(self, tag_name: str) -> bool:
        try:
            tags = self.driver.find_element(
                By.XPATH, "//span[@class='tag__text' and text()='Тестовый тэг']"
            )
            if tags.text == "Тестовый тэг":
                return True
            else:
                return False
        except Exception as e:
            print(e)


class AssetManager:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_asset(self, asset_name: str, address: str, dropdowns_dict: dict):
        self.driver.find_element(By.XPATH, "//a[text()='Активы']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Добавить актив']").click()

        self.driver.find_element(By.NAME, "name").send_keys(asset_name)
        self.driver.find_element(By.NAME, "Address").send_keys(address)

        for xpath, value in dropdowns_dict.items():
            select_dropdown_func(self.driver, xpath, value)

        self.driver.find_element(By.CLASS_NAME, "select-tag-input__icon").click()
        self.driver.find_element(By.CLASS_NAME, "checkbox__icon").click()
        self.driver.find_element(By.XPATH, "//button[text()='Создать']").click()


class DeleteAssets:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def delete_asset(self, select_all: str, delete_button: str):
        self.driver.find_element(By.XPATH, "//a[text()='Активы']").click()
        delete_assets_func(self.driver, select_all, delete_button)

    def delete_tags(self, select_all: str, delete_button: str):
        self.driver.find_element(By.XPATH, "//div[text()='Инструменты']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Теги']").click()
        delete_assets_func(self.driver, select_all, delete_button)


def main():
    driver = WebDriver()
    driver.get("https://0.0.0.0/")

    login_page = LoginPage(driver)
    login_page.login("admin", "admin")

    driver.find_element(By.CLASS_NAME, "license-expires-button-cancel").click()

    tag_manager = TagManager(driver)
    tag_manager.add_tag("Тестовый тэг", "Описание тестового тэга")

    asset_manager = AssetManager(driver)
    dropdowns_dict = {
        "//input[@name='AddressType']/parent::div": "IPv4",
        "//input[@name='importanceType']/parent::div": "IMPORTANCE_TYPE_HIGH",
        "//input[@name='osType']/parent::div": "OPERATING_SYSTEM_TYPE_MACOS",
        "//input[@name='deviceType']/parent::div": "DEVICE_TYPE_TERMINAL",
    }
    asset_manager.add_asset("Тестовый актив", "147.45.235.190", dropdowns_dict)

    while True:
        user_input = input("Вы хотите удалить тестовые данные? [y/n]: ")
        if user_input.lower() in ["y", "yes"]:
            delete_assets = DeleteAssets(driver)
            delete_assets.delete_asset(
                "//input[@aria-label='Select all rows']", "//p[text()='Удалить']"
            )
            delete_assets.delete_tags("//span[@class='checkbox__icon']", "//div[text()='Удалить']")
            print("Тестовые данные удалены\nПрограмма выполнена")
            break
        elif user_input.lower() in ["n", "no"]:
            print("Программа выполнена")
            break
        else:
            print("Неверный ввод, пожалуйста, введите 'y' или 'n'.")

    time.sleep(120)
    driver.quit()


if __name__ == "__main__":
    main()
