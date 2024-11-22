import time
from selenium import webdriver
from selenium.webdriver.common.by import By

login = 'login'
password = 'password'

def run():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.pythonanywhere.com/login/?next=/consoles/')
    driver.find_element(By.ID, 'id_auth-username').send_keys(login)
    driver.find_element(By.ID, 'id_auth-password').send_keys(password)
    driver.find_element(By.ID, 'id_next').click()

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="id_consoles"]/div/div[2]/table/tbody/tr/td[2]/a/span').click()
    time.sleep(2)
    driver.get('https://www.pythonanywhere.com/user/login/files/home/login/file.py?edit')
    driver.find_element(By.XPATH, '//*[@id="id_editor_buttons_right"]/button[4]').click()
    time.sleep(30)


run()