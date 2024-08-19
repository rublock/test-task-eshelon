from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def delete_assets_func(driver, select_all, delete_button):
    try:
        driver.find_element(By.XPATH, select_all).click()
        delete_icon = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, delete_button))
        )
        delete_icon.click()
    except Exception as e:
        print("Ошибка:", e)

    try:
        delete_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Удалить']"))
        )
        delete_button.click()
    except Exception as e:
        print("Ошибка:", e)
