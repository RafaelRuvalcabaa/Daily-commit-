###
# 03 - Cuantificadores 
# Los cuantificadores se utilizan para especificar cuantas ocurrencias de un caracter o grupo de caracteres se deben encontrar en una cadena.

import re 

# *: Puede aparecer 0 o mas veces 

text = "aaaba"

pattern = "a*"

matches = re.findall(pattern, text)

print(matches)


# Ejercicio 1: 
# ¿Cuantas palabras tienen de 0 a mas "a" y despues una b?

# +: Una o mas veces 


text = "dddd aaa ccc aa bb casa"

pattern = "a+"

matches = re.findall(pattern,text)

print(matches)


# ? : Cero o una vez 

text = "aabacb"

pattern = "a?b"

matches = re.findall(pattern,text)

print(matches)