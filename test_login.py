from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar el WebDriver para Edge
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)

# Caso de Prueba 1: Buscar "Python" en W3Schools
def test_search_python():
    driver.get("https://www.w3schools.com/")
    driver.maximize_window()
    time.sleep(2)
    
    search_box = driver.find_element(By.ID, "search2")
    search_box.send_keys("Python")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    
    results = driver.find_elements(By.CLASS_NAME, "contentcontainer")
    assert len(results) > 0, "No se encontraron resultados para 'Python'"
    print("Caso de Prueba 1: Búsqueda de 'Python' exitosa.")

# Caso de Prueba 2: Verificar que el botón de 'Tutorials' está presente
def test_tutorials_button():
    driver.get("https://www.w3schools.com/")
    time.sleep(2)
    
    tutorials_button = driver.find_element(By.LINK_TEXT, "Tutorials")
    assert tutorials_button.is_displayed(), "El botón 'Tutorials' no está visible"
    print("Caso de Prueba 2: Botón 'Tutorials' encontrado correctamente.")

# Caso de Prueba 3: Navegar a la sección de Python Tutorial
def test_navigate_python_tutorial():
    driver.get("https://www.w3schools.com/")
    time.sleep(2)

    search_box = driver.find_element(By.ID, "search2")
    search_box.send_keys("Python")
    search_box.send_keys(Keys.RETURN)
    
    python_link = driver.find_element(By.LINK_TEXT, "Start learning Python now »")
    python_link.click()
    time.sleep(2)
    
    assert "Introduction to Python" in driver.title, "No se navegó correctamente a la página de Python Tutorial"
    print("Caso de Prueba 3: Navegación al tutorial de Python exitosa.")

# Ejecutar los casos de prueba
test_search_python()
test_tutorials_button()
test_navigate_python_tutorial()

# Cerrar el navegador
driver.quit()
