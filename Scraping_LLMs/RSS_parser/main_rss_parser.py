from modulo_read_rss import extraer_datos
from aoairespuestas import preguntas
from creardocx import crear_docx

urls = [
    "https://www.microsoft.com/en-us/research/feed/",
]

for url in urls:
    datos = extraer_datos(url)
    if datos:
        msg = ""
        for entrada in datos:
            print(f"Título: {entrada['titulo']}")
            print(f"Enlace: {entrada['link']}")
            print(f"Autor: {entrada['autor']}")
            print(f"Fecha de publicación: {entrada['fecha_publicacion']}")
            print(f"Descripción: {entrada['descripcion']}")
            
            msg += f"Título: {entrada['titulo']}\n"
            msg += f"Enlace: {entrada['link']}\n"
            msg += f":Autor {entrada['autor']}\n"
            msg += f":Fecha de publicación {entrada['fecha_publicacion']}\n"
            msg += f":Descripción {entrada['descripcion']}\n"
            print("-" * 80)
            
        respuesta, tokens_enviados, tokens_recibidos, tokens_totales = preguntas(msg)
        crear_docx(respuesta, tokens_enviados, tokens_recibidos, tokens_totales)
        
    else:
        print(f"No se pudieron obtener datos del feed: {url}")