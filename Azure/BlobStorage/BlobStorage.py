import requests
import json  

# Datos que quieres subir  
data = {  
    "key1": "value1",  
    "key2": "value2"  
}  

# Convertir a JSON  
json_data = json.dumps(data)  

# Nombre del archivo
blob_name = "mi_archivo.json"  

# URL del blob con el token SAS  
sas_token = "sas_token"  
storage_account_name = "storage_account_name"  
container_name = "output"  
url = f"https://{storage_account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"  

# Headers para la solicitud HTTP  
headers = {  
    "x-ms-blob-type": "BlockBlob",  
    "Content-Type": "application/json"  
}  

# Realizar la solicitud PUT para subir el archivo  
response = requests.put(url, headers=headers, data=json_data)  

if response.status_code == 201:  
    print("Archivo subido exitosamente")  
else:  
    print(f"Error al subir el archivo: {response.status_code}")  
    print(response.text)  
