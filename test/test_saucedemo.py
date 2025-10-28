import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from selenium.webdriver.common.by import By
from utils.helpers import login_saucedemo, get_driver

@pytest.fixture
def driver():
    #configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver):
    #logueo de usuario con user y password
    #click al boton de login
    login_saucedemo(driver)

    #verificar el titulo de la pagina(ventanita)
    assert "/inventory.html" in driver.current_url                  

def test_catalogo(driver):
    #logueo de usuario con user y password
    #click al boton de login
    login_saucedemo(driver)

    #verificar el titulo del body del html
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'

    #comprobar si existen productos en la pagina visibles (len())
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0

    #verificar elementos importantes de la pagina 
    boton_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    assert boton_menu.is_displayed()

    filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    assert filtro.is_displayed()

def test_carrito(driver):
    #logueo de usuario con user y password
    #click al boton de login
    login_saucedemo(driver)

    #agregar producto a carrito
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0

    products[0].find_element(By.TAG_NAME, 'button').click()

    #verificar que el producto se agregó
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == "1"  
