import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

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

#def test_catalogo():
    #logueo de usuario con user y password
    #click al boton de login
    #verificar el titulo del body del html
    #comprobar si existen productos en la pagina visibles (len())
    #verificar elementos importantes de la pagina 

#def test_carrito():
    #logueo de usuario con user y password
    #click al boton de login
    #llevarme a pagina del carrito de compras
    #incremento del carrito al agregar producto
    #comprobar que en el carrito aparezca el producto
