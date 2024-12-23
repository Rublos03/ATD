from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuración de Selenium
driver = webdriver.Edge()

# Cargar la página
url = "https://es.statista.com/estadisticas/730785/vehiculos-electricos-matriculados-por-comunidad-autonoma-espana/"
driver.get(url)

# Esperar a que se cargue el contenido dinámico
time.sleep(5)

# Buscar la tabla o los datos de vehículos eléctricos
try:
    # Localiza elementos por etiquetas o clases específicas
    table = driver.find_element(By.CLASS_NAME, "dataTables_wrapper")  # Cambiar si es necesario
    rows = table.find_elements(By.TAG_NAME, "tr")
    
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        data = [col.text.strip() for col in columns]
        print(data)
except Exception as e:
    print(f"Error al extraer datos: {e}")
finally:
    driver.quit()