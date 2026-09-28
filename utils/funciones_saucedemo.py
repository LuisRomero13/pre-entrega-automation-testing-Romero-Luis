from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_SAUCEDEMO = "https://www.saucedemo.com/" 

# Abre la página principal de SauceDemo.
def abrir_saucedemo(driver): 
        driver.get('https://www.saucedemo.com') 

# Completa el formulario de login con las credenciales recibidas.
def realizar_login(driver, usuario, contraseña): 
    campo_usuario = driver.find_element(By.ID, 'user-name')
    campo_usuario.send_keys(usuario) 
    campo_contraseña = driver.find_element(By.ID, "password") 
    campo_contraseña.send_keys(contraseña) 
    take_screenshot(driver, "captura2.png")
    boton_login = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    boton_login.click() 

# Espera hasta que la página de inventario esté cargada.
def esperar_inventario(driver): 
    WebDriverWait(driver, 10).until( EC.url_contains("/inventory.html") ) 
    

"""
Toma una captura de pantalla y la guarda.

Args:
    driver: Instancia del WebDriver
    filename: Nombre del archivo donde guardar la captura
"""
def take_screenshot(driver, filename):
    try:
        driver.save_screenshot(f"screenshots/{filename}")
        print(f"Captura de pantalla guardada como {filename}")
    except Exception as e:
        print(f"Error al guardar la captura de pantalla: {e}")

#  Obtiene el nombre y precio del primer producto visible en el catálogo.
# def obtener_primer_producto(driver): 
#     producto = WebDriverWait(driver, 10).until( EC.visibility_of_element_located( (By.CLASS_NAME, "inventory_item") ) ) 
    
#     nombre = producto.find_element( By.CLASS_NAME, "inventory_item_name" ).text 
#     precio = producto.find_element( By.CLASS_NAME, "inventory_item_price" ).text 
#     return nombre, precio