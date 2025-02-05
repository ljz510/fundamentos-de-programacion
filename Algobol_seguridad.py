"""Debido a los recientes incidentes de público conocimiento, la ALGOBOL se vio obligada a reprogramar el clásico de la programación Argentina. 
La ALGOBOL tiene una lista de las posibles fechas para reprogramar el encuentro, pero debe garantizar que exista un operativo de seguridad adecuado para prevenir posibles incidentes.

Dada la función hay_seguridad(fecha) que devuelve True si una fecha tiene suficiente seguridad; y una lista de Python con fechas, se pide:
Escribir una función recursiva que elimine todas las fechas posibles donde la seguridad no es suficiente para cubrir el evento.

Nota: La funcion debe ser in-place (no devolver una nueva lista) y se debe mantener el orden relativo de las fechas."""

#hay_seguridad (fecha): -> True si la fecha tiene seguridad, False caso contrario#

def seguridad_insuficiente(lista_fechas):
  if len(lista_fechas) == 0:
    return 
  else:
    fecha = lista_fechas[0]
    if not hay_seguridad(fecha):
      lista_fechas.remove(fecha) #remuevo la fecha que no cuenta con la seguridad suficiente#
      seguridad_insuficiente(lista_fechas)
    else:
      return seguridad_insuficiente(lista_fechas[1:])#si tiene seguridad, la dejo en la lista#
  
