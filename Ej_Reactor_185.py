"""Implementar la siguiente clase Reactor. Las excepciones del ejemplo corresponden a una excepción en la ejecución.
El combustible solo se puede agregar con al menos 50% de refrigeración, y al agregar combustible se reduce la refrigeración un 25%.
>>> reactor = Reactor()                                >>> print(reactor)
>>> print(reactor)                                     Reactor (refrigeración = 75%, combustible = 1/3)
Reactor (refrigeración = 0%, combustible = 0/3)        >>> reactor.agregar_combustible()
>>> reactor.agregar_combustible()                      >>> reactor.controlar_refrgeracion(100)
Exception: No hay al menos 50% de refrigeración        >>> reactor.agregar_combustible()
>>> reactor.controlar_refrgeracion(100)                 >>> reactor.agregar_combustible()
>>> print(reactor)                                     Exception: El reactor ya está lleno!
Reactor (refrigeración = 100%, combustible = 0/3)      >>> reactor.controlar_refrgeracion(1989)
>>> reactor.agregar_combustible()                      Exception: El control va entre 0 y 100"""

class Reactor:

    def __init__(self):
        self.tanque_refrigeracion = 0
        self.tanque_combustible = 0

    def agregar_combustible (self):

        if self.tanque_refrigeracion >= 50:
            if self.tanque_combustible < 3:
                self.tanque_combustible += 1
                self.tanque_refrigeracion -= 25
            else:
                raise Exception("reactor lleno")
        else:
            raise Exception("no hay al menos 50% de refrigeracion")



    def controlar_refrigeracion (self, agregar_refrigeracion):

        if 0 <= agregar_refrigeracion <= 100:
            self.tanque_refrigeracion += agregar_refrigeracion
        else:
            raise Exception("solo entre 0 y 100")

    def __str__(self):

        return f"Reactor(refrigeración = {self.tanque_refrigeracion}%, combustible = {self.tanque_combustible}/3)" 
