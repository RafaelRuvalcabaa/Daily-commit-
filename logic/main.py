def fantasticos():
    """
    Funcion que cuenta cuantas veces existe J and R en un texto 
    """
    contadorJ = 0
    contadorR = 0

    texto = input("Ingresa un texto: ")
    texto = texto.upper()
    for letra in texto:
        if letra == "j":
            contadorJ += 1
        elif letra == "r":
            contadorR += 1
    
    return contadorJ == contadorR



def check_is_balanced(text):
    """
    Docstring for check_is_balanced
    Aqui con mejor logica usando una funcion de py llamada count y hace lo mismo que usan un for para recorrer
    """
    text = text.upper()

    count_r = text.count("R")
    count_j = text.count("J")

    print(f"count_r: {count_r} conunt_j: {count_j}")

   
    # If count_r == count_j:
    # return True; 
    # else: 
    # return False; 
    # || No hacer eso nunca ya que con lo siguente es lo mismo. 


    return count_j == count_r

  
