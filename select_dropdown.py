from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def select_dropdown_func(driver, xpath, value):
    try:
        dropdown_wrapper = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        dropdown_wrapper.click()

        option_to_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, value))
        )
        option_to_select.click()
    except Exception as e:
        print(f"Ошибка при выборе опции: {e}")


def delete_assets(driver, xpath):
    try:
        driver.find_element(
            By.XPATH, "//input[@type='checkbox' and @aria-label='Select all rows']"
        ).click()
        delete_icon = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        delete_icon.click()

    except Exception as e:
        print("Ошибка:", e)

    try:
        delete_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'button_full-red') and text()='Удалить']")
            )
        )
        delete_button.click()
    except Exception as e:
        print("Ошибка:", e)
