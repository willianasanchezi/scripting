from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def extraer_datos_proyecto_selenium(url):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Opcion para que no se abra la ventana del navegador (opcional)

        driver = webdriver.Chrome(options=options) # O Firefox(), según tu navegador
        driver.get(url)

        # Ajuste tiempo de espera según la página
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.card.card--project"))  # Reemplaza con tu selector CSS
        )

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        proyectos = []
        for article in soup.find_all("article", class_="card card--project"):
            # ... (el resto del código de extracción es igual al anterior)
            tipo = article.find("span", class_="card__label").text.strip()
            titulo = article.find("h3", class_="card__heading").a.text.strip()
            enlace = article.find("h3", class_="card__heading").a["href"]
            descripcion = article.find("p").text.strip()

            proyectos.append({
                "tipo": tipo,
                "titulo": titulo,
                "enlace": enlace,
                "descripcion": descripcion
            })


        driver.quit()  # Cierra el navegador
        return proyectos

    except Exception as e:
        print(f"Error: {e}")
        return None

url_de_la_pagina = "https://www.microsoft.com/en-us/research/projects/"  # Reemplaza con la URL real
datos_proyectos = extraer_datos_proyecto_selenium(url_de_la_pagina)

if datos_proyectos:
    for proyecto in datos_proyectos:
        print("Tipo:", proyecto["tipo"])
        print("Título:", proyecto["titulo"])
        print("Enlace:", proyecto["enlace"])
        print("Descripción:", proyecto["descripcion"])
        print("-" * 20)
else:
    print("No se pudieron obtener los datos de los proyectos.")