from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login_saucedemo(username_value, password_value):
    # Инициализация драйвера (предполагается, что у вас установлен ChromeDriver)
    driver = webdriver.Chrome()

    try:
        # Переход на страницу
        driver.get("https://www.saucedemo.com/")

        # Находим поле для ввода имени пользователя
        username_field = driver.find_element(By.ID, "user-name")
        # Находим поле для ввода пароля
        password_field = driver.find_element(By.ID, "password")
        # Находим кнопку входа (submit)
        submit_button = driver.find_element(By.ID, "login-button")

        # Вводим данные
        username_field.send_keys(username_value)
        password_field.send_keys(password_value)

        # Нажимаем кнопку
        submit_button.click()

        # Можно добавить задержку для проверки результата
        time.sleep(3)

    finally:
        # Закрываем браузер
        driver.quit()

