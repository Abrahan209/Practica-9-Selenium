import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

# Caso de Prueba 1: Buscar "Python" en W3Schools
def test_search_python(driver):
    driver.get("https://www.w3schools.com/")
    time.sleep(2)
    
    search_box = driver.find_element(By.ID, "search2")
    search_box.send_keys("Python")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    
    results = driver.find_elements(By.CLASS_NAME, "contentcontainer")
    assert len(results) > 0, "No se encontraron resultados para 'Python'"

# Caso de Prueba 2: Verificar que el botón de 'Tutorials' está presente
def test_tutorials_button(driver):
    driver.get("https://www.w3schools.com/")
    time.sleep(2)
    
    tutorials_button = driver.find_element(By.LINK_TEXT, "Tutorials")
    assert tutorials_button.is_displayed(), "El botón 'Tutorials' no está visible"

# Caso de Prueba 3: Navegar a la sección de Python Tutorial
def test_navigate_python_tutorial(driver):
    driver.get("https://www.w3schools.com/")
    time.sleep(2)

    search_box = driver.find_element(By.ID, "search2")
    search_box.send_keys("Python")
    search_box.send_keys(Keys.RETURN)
    
    python_link = driver.find_element(By.LINK_TEXT, "Start learning Python now »")
    python_link.click()
    time.sleep(2)
    
    assert "Python" in driver.title, "No se navegó correctamente a la página de Python Tutorial"
