import requests 

from aoairespuestas import preguntas
from creardocx import crear_docx

urls = [
    "https://www.microsoft.com/en-us/research/feed/",
]

for url in urls:
    
    response = requests.get(url)  
    
    if response.status_code == 200:
        content = response.text
        print(content)  
        respuesta, tokens_enviados, tokens_recibidos, tokens_totales = preguntas(content)
        print(respuesta)
        crear_docx(respuesta, tokens_enviados, tokens_recibidos, tokens_totales)
        print("-" * 80)
    else:  
        print(f"Error al obtener la página: {response.status_code}")  
    
    
