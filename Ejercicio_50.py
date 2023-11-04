#Escribir una función que, dada una lista de nombres y una letra, devuelva una lista con todos los nombres que empiezan por dicha letra. La función debe ignorar mayúsculas y minúsculas; es decir, tanto "alan" como "Alan" empiezan con "A" (y con "a").

def nombres (listas_nombres, letra):
    nombres = []
    letra = letra.lower()#todo en minuscula#
    for nombre in listas_nombres:
        cada_nombre = nombre.lower()
        if letra == cada_nombre[0]:
            nombres.append(cada_nombre)
        
    return nombres    
            
