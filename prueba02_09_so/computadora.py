from dispositivo import Dispositivo

class Computadora(Dispositivo):
    def _init_(self, marca, modelo, precio, ram):
        super()._init_(marca, modelo, precio)
        self.ram = ram

    def descripcion(self):
        return f"Computadora marca {self.marca}, modelo {self.modelo}, RAM: {self.ram} GB"