from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del controlador
driver = webdriver.Edge()

try:
    # Configuración del tiempo de espera
    wait = WebDriverWait(driver, timeout=10)

    # Abrir la página web
    driver.get("https://aqicn.org/city/spain/es/")

    # Hacer clic en el botón inicial
    buscar = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/center/table/tbody/tr/td[6]/center/a/div/span")))
    buscar.click()

    # Encontrar el campo de búsqueda y escribir "Valencia"
    buscador = wait.until(EC.presence_of_element_located((By.ID, "full-page-search-input")))
    buscador.send_keys("Valencia")
    buscador.send_keys(Keys.RETURN)

    # Esperar a que los resultados estén cargados
    wait.until(EC.presence_of_element_located((By.ID, "searchResults")))

    # Hacer clic en la primera opción
    first_option = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[2]/div/center/div/div[1]/center/table/tbody/tr[2]/td/div/div/a[1]")))
    first_option.click()

    # Extraer los datos necesarios
    city = wait.until(EC.presence_of_element_located((By.ID, "aqiwgttitle1"))).text  # Cambié "_istranslated=1" por "h2"
    num = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "aqivalue"))).text
    calidad = wait.until(EC.presence_of_element_located((By.ID, "aqiwgtinfo"))).text
    act = wait.until(EC.presence_of_element_located((By.ID, "aqiwgtutime"))).text
    temp = wait.until(EC.presence_of_element_located((By.ID, "aqiwgtxtrainfo"))).text

    # Almacenar los datos en una lista
    resultados = [
        {"Ciudad": city, "Valor AQI": num, "Calidad del Aire": calidad, "Última Actualización": act, "Temperatura Extra": temp}
    ]

    # Imprimir los resultados
    for resultado in resultados:
        print(f"Ciudad: {resultado['Ciudad']}")
        print(f"Valor AQI: {resultado['Valor AQI']}")
        print(f"Calidad del Aire: {resultado['Calidad del Aire']}")
        print(f"Última Actualización: {resultado['Última Actualización']}")
        print(f"Temperatura Extra: {resultado['Temperatura Extra']}")
        print("-" * 50)

except Exception as e:
    print("Ocurrió un error:", e)

finally:
    driver.quit()
