import feedparser

def extraer_datos(url):
    """
    Extrae datos de una página web.
    Args:
        url (str): La URL de la página web.
    Returns:
        list: Una lista de diccionarios con los datos extraídos, o None si hay un error.
    """
    try:
        feed = feedparser.parse(url)
        if feed.bozo:
            print("Error al parsear el feed:", feed.bozo_exception)
            return None
        
        # Lista para almacenar todas las entradas
        entradas = []
        
        for entry in feed.entries:
            titulo = entry.get('title', 'Sin título')
            link = entry.get('link', 'Sin enlace')
            autor = entry.get('author', 'Autor desconocido')
            fecha_publicacion = entry.get('published', 'Fecha desconocida')
            descripcion = entry.get('description', 'Sin descripción')
            
            # Agregar la entrada a la lista
            entradas.append({
                "titulo": titulo,
                "link": link,
                "autor": autor,
                "fecha_publicacion": fecha_publicacion,
                "descripcion": descripcion
            })
        
        return entradas
    
    except Exception as e:
        print(f"Error al procesar la página {url}: {e}")
        return None