import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from utils.funciones_saucedemo import (
    abrir_saucedemo,
    realizar_login,
    esperar_inventario,
    # obtener_primer_producto,
    take_screenshot
)


@pytest.fixture
def driver():
    #  Crea una instancia del navegador para cada test y la cierra al finalizar.
    optiones = Options() 
    optiones.add_argument("--headless")
    optiones.add_argument("--disable-dev-shm-usage")
    optiones.binary_location = "/snap/chromium/current/usr/lib/chromium-browser/chrome"
    servicio = Service(executable_path="/usr/bin/chromedriver")
    navegador = webdriver.Chrome(service=servicio, options=optiones)
    navegador.implicitly_wait(5)
    yield navegador
    navegador.quit()

# Verifica que un usuario pueda iniciar sesión correctamente.
def test_login_exitoso(driver):
    # Inicia sesión con credenciales válidas
    iniciar_sesion(driver)
    #Leemos el título de la pestaña → debería salir "Swag Labs"
    print('Título:', driver.title)     
    #Validamos que el título sea el esperado (asegura que cargó bien) 
    assert driver.title == 'Swag Labs'  
    # Tomamos una captura de pantalla del inventario
    take_screenshot(driver, "captura3.png")
    # Verificar que la URL corresponda al inventario
    assert "/inventory.html" in driver.current_url
    # Verificar que aparezca el título "Products"
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title')
    assert titulo.text == "Products"
    print('Título de sección OK →', titulo.text)

# def test_catalogo(driver):
#     # Verificar que existan productos visibles
#     productos = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located(
#             (By.CLASS_NAME, "inventory_item")
#         )
#     )
#     assert len(productos) > 0
#     # Verificar elementos importantes de la interfaz
#     menu = driver.find_element(
#         By.ID,
#         "react-burger-menu-btn"
#     )
#     assert menu.is_displayed()
#     filtro = driver.find_element(
#         By.CLASS_NAME,
#         "product_sort_container"
#     )
#     assert filtro.is_displayed()
#     # Obtener nombre y precio del primer producto
#     nombre, precio = obtener_primer_producto(driver)
#     print(f"Primer producto: {nombre}")
#     print(f"Precio: {precio}")
#     assert nombre != ""
#     assert precio != ""

# Función auxiliar para realizar el login desde los tests que lo necesiten.
def iniciar_sesion(driver):
    abrir_saucedemo(driver)

    take_screenshot(driver, "captura.png")

    realizar_login(
        driver,
        "standard_user",
        "secret_sauce"
    )

    esperar_inventario(driver)