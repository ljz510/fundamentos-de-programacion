"""
Escribir una función recursiva que dada una cadena le haga un "flip" de mayúsculas, es decir, que devuelva una nueva cadena con los caracteres en minúscula transformados a mayúscula y los caracteres en mayúscula transformados en minúscula.

flip_mayusculas('AlgoRitmOs Y ProGramAcion 1') ==> 'aLGOrITMoS y pROgRAMaCION 1'
"""

def flip_mayusculas(cadena):
    lista = list(cadena)
    if len(lista) == 0:
        return ""
    else:
        letra = lista[0]
        if letra == letra.upper():
            n_letra = letra.lower()
        else:
            n_letra = letra.upper()
        return n_letra + flip_mayusculas("".join(lista[1:]))

print(flip_mayusculas('AlgoRitmOs Y ProGramAcion 1'))
