from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar el WebDriver
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)

# Abrir la página de W3Schools
driver.get("https://www.w3schools.com/")
driver.maximize_window()

time.sleep(2)  # Esperar a que la página cargue

# Buscar en la barra de búsqueda
search_box = driver.find_element(By.ID, "tnb-google-search-input")
search_box.send_keys("Python")
search_box.send_keys(Keys.RETURN)

time.sleep(2)  # Esperar los resultados

# Verificar los resultados
results = driver.find_elements(By.CLASS_NAME, "contentcontainer")
print(f"Se encontraron {len(results)} resultados para 'Python'")

# Cerrar el navegador
driver.quit()
