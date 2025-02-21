import requests
from bs4 import BeautifulSoup

def extraer_datos(url):
    """
    Extrae datos de una página web.

    Args:
        url (str): La URL de la página web.

    Returns:
        dict: Un diccionario con los datos extraídos, o None si hay un error.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        titulo = soup.find("title").text if soup.find("title") else None
        parrafos = [p.text for p in soup.find_all("p")]

        return {"titulo": titulo, "parrafos": parrafos}

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la página {url}: {e}")
        return None
    except Exception as e:
        print(f"Error al procesar la página {url}: {e}")
        return None