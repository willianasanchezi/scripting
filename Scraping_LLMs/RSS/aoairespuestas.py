import os
import requests
import json

from dotenv import load_dotenv
load_dotenv('../env/.env')

def preguntas(pregunta):
    endpoint = os.getenv("endpoint")
    apikey = os.getenv("apikey")
    context = os.getenv("context")
    temperature = os.getenv("temperature")
    top_p = os.getenv("top_p")
    max_tokens = os.getenv("max_tokens")
    
    pregunta = (f'{context}. {pregunta}')

    payload = json.dumps({
          "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": pregunta
        }
      ]
    }
    ],
    "temperature": float(temperature),
    "top_p": float(top_p),
    "max_tokens": int(max_tokens)

    })
    headers = {
      'Content-Type': 'application/json',
      'api-key': apikey
    }

    response = requests.request("POST", endpoint, headers=headers, data=payload)
    data = json.loads(response.text)

    try:  
        content = data["choices"][0]["message"]["content"]
        tokens_enviados = data["usage"]["prompt_tokens"]
        tokens_recibidos = data["usage"]["completion_tokens"]
        tokens_totales = data["usage"]["total_tokens"]
        
    except KeyError as e:  
        print(f"La clave no existe: {e}")  
        content = None
        tokens_enviados = tokens_recibidos = tokens_totales = 0
    except IndexError as e:  
        print(f"El índice no existe: {e}")  
        content = None
        tokens_enviados = tokens_recibidos = tokens_totales = 0
            
    return content, tokens_enviados, tokens_recibidos, tokens_totales