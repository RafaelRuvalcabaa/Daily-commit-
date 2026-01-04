#Ejemplo diccionario 

persona = {
    "nombre": "Rafa",
    "edad": 23,
    "es_estudiante": False, 
    "calificaciones": [9,10,10],
    "socials":{
        "twitter": "@rafa",
        "facebook": "@rafa"
    }
}


#Para acceder a los valores

print(persona["nombre"])
print(persona["calificaciones"][2])

#Cambiar valores al acceder 

persona["socials"]["facebook"] = "@rafita "

print(persona["socials"])


print(persona)