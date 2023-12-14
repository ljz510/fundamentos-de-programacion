"""Escribir una función validar_contraseña que reciba una palabra clave y un número de intentos n. Dicha función debe pedir al usuario que ingrese la contraseña un máximo de n veces. En caso de que la contraseña ingresada coincida con la recibida por la función, se devuelve True, caso contrario se devuelve False."""

def validar_contraseña (clave_correcta, intentos):
    for i in range (1, intentos + 1):
        contraseña = input(f"ingrese la clave correcta")
        if contraseña == clave_correcta:
            print ("clave correcta")
            return True
        else:
            intentos_restantes = intentos - 1
            print (f"le restan {intentos_restantes} intentos")
    print ("numero maximo de intentos alcanzado")        
    return False    
    
    
clave_correcta = "mi"
intentos = 3
resultado = validar_contraseña(clave_correcta, intentos)
