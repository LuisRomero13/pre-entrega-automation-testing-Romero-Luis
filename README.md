# Pre-entrega Proyecto Final - Automatización de Testing
Este proyecto implementa una automatización de pruebas para el sitio SauceDemo, utilizando Selenium WebDriver y Python.

## 🎯 Propósito del Proyecto
El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo:
- Login con credenciales válidas e inválidas
- Verificación del catálogo de productos
- Interacción con el carrito de compras (añadir productos y verificar su contenido)
- Cierre de sesión

## 🛠️ Tecnologías Utilizadas
- **Python:** Lenguaje de programación principal
- **Pytest:** Framework de testing para estructurar y ejecutar pruebas
- **Selenium WebDriver:** Para la automatización de la interfaz web
- **Git/GitHub:** Para control de versiones y compartir el código

## 📁 Estructura del Proyecto
```
pre-entrega-automation-testing-Romero-Luis/
├── tests/test_saucedemo.py # Casos de prueba automatizados correspondientes a las consignas
├── utils/funciones_saucedemo.py # funciones auxiliares reutilizables
├── screenshots/ # Capturas de pantalla (se crea automáticamente)
└── extras/ # NO PERTENECE a la pre-entrega pero util para mi aprendizaje con python
```
## ⚙️ Instalación de Dependencias
1. Asegúrate de tener Python 3.12 o superior instalado.
2. Instala las dependencias necesarias:
pip install selenium pytest pytest-html

3. Descarga el WebDriver correspondiente a tu navegador. En mi caso instalé:
Chromium

4. Asegúrate de que el WebDriver esté en tu PATH o especifica su ubicación en el código.

## ▶️ Ejecución de las Pruebas
**Para ejecutar todas las pruebas:**
.venv/bin/python3 -m pytest tests/test_saucedemo.py -s

**Para generar un reporte HTML:**
.venv/bin/python3 -m pytest tests/test_saucedemo.py -s -v --html=reports/reporte.html

## ✅ Funcionalidades Implementadas

1. Automatización de Login:
   - Caso de éxito con credenciales válidas
   - Caso de fallo con credenciales inválidas

2. Verificación del Catálogo:
   - Comprobación del título de la página
   - Verificación de presencia de productos
   - Verificion de elementos importantes de la interfaz (menu, filtro y carrito)

3. Interacción con el Carrito:
   - Añadir producto al carrito
   - Verificar que el contador se incremente
   - Navegar al carrito
   - Comprobar que el producto añadido aparezca correctamente

4. Cierre de Sesión:
   - Verificar que el usuario pueda cerrar sesión correctamente

## ✨ Características Adicionales
Capturas de pantalla automáticas, conformandose asi estos archivos:
   - **captura.png:** carga exitosamente a la página de sauce demo
   - **captura2.png:** relleno de formulario de sesion incorrectamente
   - **captura3.png:** redirección a la pagina de productos luego de iniciar sesion
   - **captura4.png:** redirección a la pagina de carrito luego de agregar un producto

Funciones auxiliares reutilizables: En el archivo funciones_saucedemo.py.

## 👤 Autor
Luis Romero

## 📝 Notas
Este proyecto fue desarrollado como pre-entrega para el curso de Automatización de Testing.

Todas las pruebas están diseñadas para funcionar con el sitio web SauceDemo en su versión actual.

**IMPORTANTE:** estas lineas de código fueron agregadas solo porque utilizo WSL (no tiene interfaz grafica) y no encontraba mi webDriver:
```
    optiones.add_argument("--headless")
    optiones.add_argument("--disable-dev-shm-usage")
    optiones.binary_location = "/snap/chromium/current/usr/lib/chromium-browser/chrome"
    servicio = Service(executable_path="/usr/bin/chromedriver")
```