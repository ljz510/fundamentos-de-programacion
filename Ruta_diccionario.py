'''Sea un diccionario recursivo, cuyas claves son cadenas y sus valores pueden ser cadenas o diccionarios recursivos.
Se define la ruta de un valor en el diccionario como la sucesión de claves para encontrar el valor, separadas por el carácter .

Escribir la función get(d, ruta)
que recibe un diccionario recursivo y una ruta, y devuelve el valor que se encuentra en la ruta indicada. Se puede asumir que la ruta es válida y el valor buscado existe en el diccionario. '''

def get(d, ruta):
    r = ruta.split('.')
    if len(r) == 1:
        return d[r[0]]
    else:
        if r[0] in d: #puesto que el valor buscado va a existir siempre en el diccionario mo considere necesario un else#
            return get(d[r[0]], '.'.join(r[1:]))
