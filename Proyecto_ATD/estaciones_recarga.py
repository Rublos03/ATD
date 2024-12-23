from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
try:
    wait = WebDriverWait(driver, timeout=60)
    driver.get("https://map.electromaps.com/es/")


    busqueda = driver.find_element(By.ID, "tipoBusqueda")
    busqueda.click()
    estaciones = driver.find_element(By.XPATH, "//*[@id='tipoBusqueda']/option[3]")
    estaciones.click()

except Exception as e:
    print("Ocurrió un error:", e)

