from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def check_elements():
    driver = webdriver.Chrome()

    try:
        # Переход на страницу
        driver.get("https://www.saucedemo.com/")

        # Попытка найти элементы
        try:
            username_field = driver.find_element(By.ID, "user-name")
            password_field = driver.find_element(By.ID, "password")
            submit_button = driver.find_element(By.ID, "login-button")
            # Если все элементы найдены, выводим сообщение
            print("Элементы найдены")
        except NoSuchElementException:
            print("Один или несколько элементов не найдены")
    finally:
        driver.quit()

# Вызов функции
# check_elements()
