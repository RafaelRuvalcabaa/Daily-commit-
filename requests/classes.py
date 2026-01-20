# Introduccion a clases en Python 

# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.

# Nos permiten agrupar datos y funcionalidades relacionadas en una sola entidad.

# Ejemplo basico de una clase en Python:  

class Coche: 
    # Atributo de clase (comparten todos los objetos).
    tipo  = "vehiculo de cuatro ruedas"
    ruedas = 4 
    # metodo especial (constructor) que se llama al crear un objeto. Al llamar a la clase, se ejecuta este metodo.
    def __init__(self, marca, color, año): # El self se refiere al objeto asi sismo.
        self.marca = marca
        self.color = color
        self.año = año

    def arrancar(self):
        print(f"El coche {self.marca} ha arrancado.")


# Se pueden crear indefinidamente objetos de la clase Coche.
miCoche = Coche("toyota", "rojo", 2020)

# Accedemos a los atributos y metodos del objeto. Usando un punto. Por ejemplo: usamos la funcion arrancar, donde arrancar ya esta estipulado en la clase Coche.
coche_ulises = Coche("Seat", "azul fiordo", 2025)


# Mostramos los atributos del objeto miCoche
print(f"Mi coche es un {miCoche.marca} de color {miCoche.color} del año {miCoche.año}.")


# Usamos el metodo arrancar de la clase Coche en los dos objetos creados.
miCoche.arrancar()
coche_ulises.arrancar()



# Encapsulacion: es ocultar los detalles internos de una clase y exponer solo lo necesario.


# Crear un clase para encapsular para llamar a la API de OpenAI GPT-4o o DeepSeek. 


import requests

class API: 
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = url 
        self.model = model 
        
        def __call__(self, prompt):
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }

            data = { 
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}]
            }

            response = requests.post(self.url, headers=headers, json=data)
            return response.json()
        
# Usar la clase API para llamar a OpenAI GPT-4o

OPENAI_API_KEY = API("OPENAIAPI_KEY", "https://api.openai.com/v1/chat/completions", "gpt-4o")