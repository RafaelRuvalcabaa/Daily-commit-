###
# ------------ Meta caracteres 
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones reguales. 
### 

import re 

#1.- El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea

text = "Hola mundo, H0la de nuevo, H#la otra vez"

pattern = "H.la"
 

found = re.findall(pattern, text)

if(found):
    print(found)
else: 
    print("No se encontro ninguna coincidencia...")


text = "casa caasa cosa cisa cessa cesa causa"


pattern = "c.sa"

found = re.findall(pattern, text)

if(found):
    print(found)
    print(f"Se encotró {len((found))} veces")
else: 
    print("No se encontraron coincidencias....")