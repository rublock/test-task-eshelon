from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def select_dropdown_func(driver, dropdowns_dict):
    for xpath, value in dropdowns_dict.items():
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
