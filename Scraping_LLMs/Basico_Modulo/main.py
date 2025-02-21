from modulo_scraper import extraer_datos

urls = [
    "https://techcommunity.microsoft.com/category/ai/blog/azure-ai-services-blog",
    "https://azure.microsoft.com/en-us/blog/product/azure-openai-service/",
    "https://techcommunity.microsoft.com/category/ai/blog/machinelearningblog",
    "https://www.microsoft.com/en-us/research/search/?facet%5Btax%5D%5Bmsr-content-type%5D[]=msr-project&q=",
]

for url in urls:
    datos = extraer_datos(url)
    if datos:
        print(f"Datos de {url}:")
        print(f"  Título: {datos['titulo']}")
        print(f"  Párrafos: {datos['parrafos']}")
    print("-" * 20)