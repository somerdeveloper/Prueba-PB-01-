from dispositivo import Dispositivo

# Clase hija que representa una tablet
class Tablet(Dispositivo):
    def _init_(self, marca, modelo, precio, pulgadas):
        super()._init_(marca, modelo, precio)
        self.pulgadas = pulgadas

    def descripcion(self):
        return f"Tablet marca {self.marca}, modelo {self.modelo}, Pantalla: {self.pulgadas} pulgadas"