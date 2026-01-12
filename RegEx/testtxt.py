# /b coincide con el principio o final de una palabra 

import re 
text = "casa coche perro acasa casado casada casa cosa cosas"

pattern = r"\bc.sa\b"

found = re.findall(pattern, text)

print(found)