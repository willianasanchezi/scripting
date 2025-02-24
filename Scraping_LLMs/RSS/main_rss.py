from modulo_read_rss import extraer_datos

urls = [
    "https://www.microsoft.com/en-us/research/feed/",
]

for url in urls:
    datos = extraer_datos(url)
    if datos:
        for entrada in datos:
            print(f"Título: {entrada['titulo']}")
            print(f"Enlace: {entrada['link']}")
            print(f"Autor: {entrada['autor']}")
            print(f"Fecha de publicación: {entrada['fecha_publicacion']}")
            print(f"Descripción: {entrada['descripcion']}")
            print("-" * 80)
    else:
        print(f"No se pudieron obtener datos del feed: {url}")