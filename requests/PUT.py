# PUT: actualiza un recurso existente
import requests

print("\n\n\nPUT:")

try:
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json={
            "title": "Midu",
            "body": "Dev",
            "userId": 1
        }
    )

    print(response.json())
    print(f"Status code: {response.status_code}")

except requests.exceptions.RequestException as event:
    print("Error en la solicitud PUT:", event)
