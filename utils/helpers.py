from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

#Conectar driver e instalarlo
def get_driver():
    #options = Options
    #options.add_argument('--start-maximized')

    #instalacion de driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    time.sleep(3)
    return driver

#Inicio de sesion
def login_saucedemo(driver):
    driver.get(URL)

    #Ingresar las credenciales
    driver.find_element(By.NAME, 'user-name').send_keys(USERNAME)
    time.sleep(2)

    driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
    time.sleep(2)

    driver.find_element(By.ID, 'login-button').click()
    time.sleep(5)