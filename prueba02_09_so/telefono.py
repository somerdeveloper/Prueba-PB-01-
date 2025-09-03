from dispositivo import Dispositivo

# Clase hija que representa un teléfono
class Telefono(Dispositivo):
    def _init_(self, marca, modelo, precio, camara):
        super()._init_(marca, modelo, precio)
        self.camara = camara

    def descripcion(self):
        return f"Teléfono marca {self.marca}, modelo {self.modelo}, Cámara: {self.camara} MP"