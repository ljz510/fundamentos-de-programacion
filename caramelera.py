class Caramelera:

    def __init__(self,cant_caramelos):
      
        self.cant_caramelos = cant_caramelos
        self.lista_caramelos = []

    def poner_caramelos (self, caramelos_agregar):

        for i in range(1, caramelos_agregar + 1):
            if caramelos_agregar <= self.cant_caramelos:
                self.lista_caramelos.append(i)
            else:
                raise ValueError("no queda tanto lugar")
        

    def sacar_caramelos(self, caramelos_quitar):

        for _ in range(1, caramelos_quitar + 1):
            if caramelos_quitar < len(self.lista_caramelos):
                self.lista_caramelos.pop()
            else:
                raise ValueError("no quedan tantos caramelos")

    def caramelos(self):
      
        print(len(self.lista_caramelos))

    def __str__(self):
      
        return f"caramelera con {len(self.lista_caramelos)}/{self.cant_caramelos}"
