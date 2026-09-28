import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.funciones_saucedemo import (
    abrir_saucedemo,
    opciones_chrome,
    realizar_login,
    esperar_inventario,
    obtener_primer_producto,
    take_screenshot
)

@pytest.fixture
def driver():
    opciones, servicio = opciones_chrome()
    navegador = webdriver.Chrome(service=servicio, options=opciones)
    navegador.implicitly_wait(5)
    yield navegador
    navegador.quit()

# Verifica que un usuario pueda iniciar sesión correctamente. (ACTIVIDAD 1)
def test_login_exitoso(driver):
    abrir_saucedemo(driver)

    take_screenshot(driver, "captura.png")

    # Inicia sesión con credenciales válidas
    iniciar_sesion(driver)
    #Leemos el título de la pestaña → debería salir "Swag Labs"
    print('Título:', driver.title)     
    #Validamos que el título sea el esperado (asegura que cargó bien) 
    assert driver.title == 'Swag Labs'  
    # Verificar que la URL corresponda al inventario
    assert "/inventory.html" in driver.current_url
    # Verificar que aparezca el título "Products"
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title')
    assert titulo.text == "Products"
    print('Título de sección OK →', titulo.text)

# Verifica que un usuario no pueda iniciar sesión con credenciales incorrectas. (ACTIVIDAD 1)
def test_login_incorrecto(driver):
    abrir_saucedemo(driver)
 
    # Intentar iniciar sesión con credenciales incorrectas
    realizar_login(driver, "usuario_incorrecto", "contrasena_incorrecta")

    # Tomamos una captura de pantalla del error
    take_screenshot(driver, "captura2.png")

    # Verificar que aparezca un mensaje de error
    mensaje_error = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]')
    assert mensaje_error.is_displayed()
    print('Mensaje de error:', mensaje_error.text)

# Verifica que el catálogo de productos se muestre correctamente. (ACTIVIDAD 2)
def test_catalogo_y_elementos(driver):
    abrir_saucedemo(driver)

    # Inicia sesión con credenciales válidas
    iniciar_sesion(driver)

    # Tomamos una captura de pantalla del inventario
    take_screenshot(driver, "captura3.png")

    # Verificar que existan productos visibles
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0
    print(f'Se encontraron {len(productos)} productos.')

    # Obtener nombre y precio del primer producto
    nombre, precio = obtener_primer_producto(driver)
    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")
    assert nombre != ""
    assert precio != ""

    # Verificar elementos importantes de la interfaz
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed()
    filtro = driver.find_element(By.CLASS_NAME,"product_sort_container")
    assert filtro.is_displayed()
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert carrito.is_displayed()

# Verifica que un usuario pueda agregar un producto al carrito y que este se actualice correctamente. (ACTIVIDAD 3)
def test_carrito(driver):
    abrir_saucedemo(driver)

    # Inicia sesión con credenciales válidas
    iniciar_sesion(driver)

    # Agregar el primer producto al carrito
    primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item")
    boton_agregar = primer_producto.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    boton_agregar.click()

    # Verificar que el carrito tenga 1 artículo
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert carrito.text == "1"
    print('Carrito actualizado correctamente con 1 artículo.')

    # Navegar al carrito y verificar que el producto esté presente
    carrito.click()
    take_screenshot(driver, "captura4.png")
    producto_en_carrito = driver.find_element(By.CLASS_NAME, "cart_item")
    nombre_producto_carrito = producto_en_carrito.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_producto_carrito == "Sauce Labs Backpack"
    print(f'Producto en carrito: {nombre_producto_carrito}')

# Función auxiliar para realizar el login desde los tests que lo necesiten.
def iniciar_sesion(driver):
    realizar_login(
        driver,
        "standard_user",
        "secret_sauce"
    )

    esperar_inventario(driver)