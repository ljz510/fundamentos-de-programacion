'''ESCRIBIR UNA FUNCION RECURSIVA QUE RECIBA UN NUMERO NATURAL Y DEVUELVA UNA CADENA COMPUESTA POR 0 Y 1, REPRESENTANDO EL NUMERO EN NOTACIÓN BINARIA'''

def notacion_binaria(numero):
#utilizo un wrapper#
  def _notacion_binaria (numero):
    if n == 0:
      return ''
    else:
        division_entera = numero // 2
        resto = str(numero % 2)
        return resto + _notacion_binaria(division_entera)
  return _notacion_binaria(numero)[::-1]
